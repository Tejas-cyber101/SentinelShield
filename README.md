# 🛡️ SentinelShield: Advanced Intrusion Detection System

SentinelShield is a realistic simulation of a **Web Application Firewall (WAF)** and **Intrusion Detection System (IDS)**. It demonstrates how modern security tools inspect HTTP traffic, identify malicious patterns, and monitor for abusive behavioral trends.

## 🎯 Project Objectives
* **Analyze HTTP requests** from a security perspective.
* **Identify common web attacks** (SQLi, XSS, LFI) using signature-based detection.
* **Monitor traffic behavior** via Rate Limiting to prevent brute-force attacks.
* **Visualize security data** through an automated administrative dashboard.

## 🏗️ System Architecture
The system follows a modular security pipeline:
1. **WAF Engine (`main.py`)**: Intercepts and inspects all incoming requests.
2. **Rule Engine**: Matches traffic against SQLi, XSS, and LFI signatures.
3. **Behavioral Monitor**: Tracks IP frequency to detect automated scanning.
4. **Security Logger**: Generates real-time logs (`sentinel_shield_REAL.log`).
5. **Admin Dashboard (`dashboard.py`)**: A Streamlit interface for visual analytics.

## 🚀 How to Run
1. Install dependencies: `pip install flask streamlit pandas plotly`
2. Launch the system: `python run_sentinel.py`
3. Access the WAF: `http://127.0.0.1:5000`
4. Access the Dashboard: `http://localhost:8501`

## 🧪 Detection Summary
| Attack Category | Test Payload | Action |
| :--- | :--- | :--- |
| **SQL Injection** | `?id=' OR 1=1` | 403 Blocked |
| **XSS** | `?q=<script>alert(1)</script>` | 403 Blocked |
| **Brute Force** | >10 Requests/min | 429 Rate Limited |

## 📜 License
This project is licensed under the MIT License.
