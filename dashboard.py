import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="SentinelShield Admin", layout="wide")

# CUSTOM CSS: Background Image & Branding (Source 89: Visual appeal)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        color: #00FFCC;
    }
    .stMetric { background-color: rgba(30, 30, 30, 0.8); padding: 15px; border-radius: 10px; border: 1px solid #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🛡️ SentinelShield: Advanced Intrusion Detection")
st.subheader(f"Security Analyst: Tejas Bansode") # <-- ADD YOUR NAME HERE
st.markdown("---")

# --- DATA PROCESSING (Source 35: Categorize alerts) ---
def load_data():
    if not os.path.exists("sentinel_shield_REAL.log"):
        return pd.DataFrame()
    
    data = []
    with open("sentinel_shield_REAL.log", "r") as f:
        for line in f:
            # Simple parsing of the log string
            parts = line.split(" | ")
            if len(parts) >= 4:
                data.append({
                    "Timestamp": parts[0].strip("[]"),
                    "Type": parts[2].replace("Type: ", ""),
                    "IP": parts[1].replace("IP: ", ""),
                    "Request": parts[3].replace("Request: ", "")
                })
    return pd.DataFrame(data)

df = load_data()

if not df.empty:
    # --- METRICS (Source 95: Malicious requests detected) ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Threats Blocked", len(df))
    col2.metric("Unique Attackers (IPs)", df['IP'].nunique())
    col3.metric("System Status", "ACTIVE", delta="Secure")

    # --- VISUALS (Source 39: Identifying trends) ---
    c1, c2 = st.columns(2)
    
    with c1:
        st.write("### Attack Distribution")
        fig = px.pie(df, names='Type', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.write("### Recent Attack Activity")
        st.dataframe(df.tail(10), use_container_width=True)

    # --- SOURCE 94: SUMMARY TABLE ---
    st.write("### Detailed Security Logs")
    st.table(df.groupby('Type').size().reset_index(name='Total Occurrences'))

else:
    st.warning("No logs detected. Run some attacks in main.py first!")

st.sidebar.info("SentinelShield Monitoring System v1.0 [cite: 1]")
