import streamlit as st
import subprocess

st.set_page_config(page_title="AI Renewable Optimizer", layout="wide")

st.title("⚡ AI Powered Adaptive Renewable Energy Optimizer")

st.markdown("### 🌞 Solar + 💨 Wind Optimization Dashboard")

# Buttons
col1, col2 = st.columns(2)

with col1:
    run = st.button("▶ Run Dashboard")

with col2:
    show_code = st.checkbox("Show Code")

# Run your notebook
if run:
    st.info("Running your model... please wait")

    # Run your notebook file
    subprocess.run(["python", "MODEL.ipynb.py"])

    st.success("Dashboard executed")

# Hide or show code
if show_code:
    st.code(open("MODEL.ipynb.py").read())
