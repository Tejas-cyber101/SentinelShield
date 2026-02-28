import subprocess
import time
import sys

def start_project():
    print("🚀 Launching SentinelShield: Advanced Intrusion Detection System...")
    
    # 1. Start the WAF Engine (Flask) in the background
    waf_process = subprocess.Popen([sys.executable, "main.py"])
    print("✅ WAF Engine: Active on http://127.0.0.1:5000")

    # Wait a moment for the log file to initialize
    time.sleep(2)

    # 2. Start the Security Dashboard (Streamlit)
    print("✅ Security Dashboard: Initializing...")
    try:
        subprocess.run(["streamlit", "run", "dashboard.py"])
    except KeyboardInterrupt:
        print("\n🛑 Shutting down SentinelShield...")
        waf_process.terminate()

if __name__ == "__main__":
    start_project()
