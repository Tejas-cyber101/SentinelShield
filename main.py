from flask import Flask, request, abort
import time
import datetime

app = Flask(__name__)

# --- CONFIGURATION (Source 5: Rule engines) ---
SIGNATURES = {
    "SQL Injection": ["UNION SELECT", "' OR 1=1", "DROP TABLE"],
    "XSS": ["<script>", "alert(", "onerror="],
    "LFI": ["../", "/etc/passwd"]
}

# Behavioral Tracking (Source 19: Rate limiting)
ip_history = {}
LIMIT = 10  # Max requests
WINDOW = 60 # Seconds

def sentinel_inspector():
    ip = request.remote_addr
    path = request.full_path
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Rate Limiting (Source 32: Automated scanning detection)
    now = time.time()
    ip_history[ip] = [t for t in ip_history.get(ip, []) if now - t < WINDOW]
    ip_history[ip].append(now)
    
    if len(ip_history[ip]) > LIMIT:
        log_attack(timestamp, ip, "Rate Limit Exceeded", path)
        abort(429, description="Too many requests - SentinelShield blocked you.")

    # 2. Signature Inspection (Source 25: Header & Parameter inspection)
    for category, patterns in SIGNATURES.items():
        for p in patterns:
            if p.lower() in path.lower():
                log_attack(timestamp, ip, category, path)
                abort(403, description=f"SentinelShield: {category} Detected!")

def log_attack(ts, ip, cat, payload):
    # Source 36: Timestamps, IP, and labels for incident understanding
    entry = f"[{ts}] ALERT | IP: {ip} | Type: {cat} | Request: {payload}\n"
    with open("sentinel_shield_REAL.log", "a") as f:
        f.write(entry)
    print(entry.strip())

@app.before_request
def before_request():
    sentinel_inspector()

@app.route('/')
def home():
    return "<h1>Welcome to the Secure Portal</h1><p>SentinelShield is watching...</p>"

if __name__ == '__main__':
    print("SentinelShield Live on http://127.0.0.1:5000")
    app.run(port=5000)
