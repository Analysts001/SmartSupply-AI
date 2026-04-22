import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SmartSupply AI", layout="wide")

st.title("📦 SmartSupply AI")
st.write("Predictive Supply Chain Intelligence System")

# -------------------------
# DATA LOADING (SAFE + AUTO DETECT)
# -------------------------
def load_data():
    possible_files = [
        "data/cleaned_shipments.csv",
        "data/shipment_cleaned.csv",
        "data/shipment_raw.csv"
    ]
    
    for file in possible_files:
        if os.path.exists(file):
            return pd.read_csv(file)
    
    st.error("❌ No dataset found in data folder")
    return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# -------------------------
# BASIC KPI
# -------------------------
st.subheader("📊 Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Rows", len(df))
col2.metric("Columns", len(df.columns))

st.dataframe(df.head())

# -------------------------
# SIMPLE ANALYSIS
# -------------------------
if "Unit Price" in df.columns:
    st.subheader("📈 Unit Price Distribution")
    st.line_chart(df["Unit Price"])

if "Line Item Quantity" in df.columns:
    st.subheader("📦 Quantity Distribution")
    st.line_chart(df["Line Item Quantity"])

st.success("✅ App running successfully")