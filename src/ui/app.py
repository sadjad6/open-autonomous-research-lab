"""OARL Streamlit UI — Research Interface for autonomous analysis."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="OARL — Open Autonomous Research Lab",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    .agent-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        background: #667eea;
        color: white;
        margin: 0.2rem;
        font-size: 0.85rem;
    }
    .stApp { background-color: #0e1117; }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🔬 Open Autonomous Research Lab</h1>
    <p>Multi-agent AI platform for autonomous data analysis, ML experimentation, and research discovery.</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")
    analysis_mode = st.selectbox("Analysis Mode", ["Full Pipeline", "EDA Only", "ML Only", "Report Only"])
    target_col = st.text_input("Target Column", placeholder="e.g., target, label, price")
    st.divider()
    st.header("🤖 Agent Pipeline")
    agents = [
        "Orchestrator", "Planner", "Data Engineer",
        "Data Scientist", "ML Engineer", "Evaluation",
        "Research Analyst", "Knowledge Manager",
    ]
    for agent in agents:
        st.markdown(f'<span class="agent-badge">✅ {agent}</span>', unsafe_allow_html=True)

# ── Main Content ─────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📁 Upload & Analyze", "📊 Results", "📈 Metrics", "📄 Report"])

with tab1:
    st.subheader("Upload Dataset & Start Analysis")
    uploaded_file = st.file_uploader("Choose a dataset", type=["csv", "xlsx", "parquet", "json"])

    if uploaded_file:
        import pandas as pd

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xls", ".xlsx")):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        st.success(f"✅ Loaded **{uploaded_file.name}** — {df.shape[0]:,} rows × {df.shape[1]} columns")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", f"{df.shape[0]:,}")
        with col2:
            st.metric("Columns", df.shape[1])
        with col3:
            st.metric("Missing Values", f"{df.isna().sum().sum():,}")

        st.dataframe(df.head(20), use_container_width=True)

    user_request = st.text_area(
        "Analysis Request",
        placeholder="e.g., Analyze this dataset, discover insights, train predictive models, and generate a research report.",
        height=100,
    )

    if st.button("🚀 Start Analysis", type="primary", use_container_width=True):
        if not uploaded_file:
            st.error("Please upload a dataset first.")
        elif not user_request:
            st.error("Please describe your analysis request.")
        else:
            with st.spinner("🤖 Agents are working..."):
                st.info("Analysis pipeline started. In production, this triggers the full agent orchestration.")
                st.json({
                    "status": "pipeline_started",
                    "request": user_request,
                    "dataset": uploaded_file.name,
                    "mode": analysis_mode,
                    "target_column": target_col,
                })

with tab2:
    st.subheader("📊 Analysis Results")
    st.info("Results will appear here after an analysis pipeline completes.")

with tab3:
    st.subheader("📈 Model Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Model Comparison")
        sample_metrics = {
            "Model": ["Random Forest", "XGBoost", "Logistic Regression"],
            "Accuracy": [0.87, 0.89, 0.82],
            "F1 Score": [0.86, 0.88, 0.80],
            "AUC": [0.92, 0.94, 0.88],
        }
        st.dataframe(sample_metrics, use_container_width=True)
    with col2:
        st.markdown("### Performance Over Time")
        import numpy as np
        chart_data = {"iteration": range(1, 11), "score": np.random.uniform(0.75, 0.95, 10).cumsum() / np.arange(1, 11)}
        st.line_chart(chart_data, x="iteration", y="score")

with tab4:
    st.subheader("📄 Research Report")
    st.info("Generated reports will appear here. You can download them as Markdown or PDF.")
    if st.button("📥 Download Sample Report"):
        sample_report = "# Sample Research Report\\n\\n## Executive Summary\\nThis is a sample report."
        st.download_button("Download Markdown", sample_report, "report.md", "text/markdown")
