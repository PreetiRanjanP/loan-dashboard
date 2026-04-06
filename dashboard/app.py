import sys
sys.path.insert(0, 'D:\\DATA ANALYST BOOTCAMP\\Loan Dashboard')

import streamlit as st
import pandas as pd
import plotly.express as px
from analysis.kpi import get_kpis
from analysis.trends import (monthly_disbursement, branch_performance,
                              loan_status_distribution, loan_type_breakdown)

st.set_page_config(page_title="Loan Analytics Dashboard",
                   page_icon="💰", layout="wide")

@st.cache_data
def load_data():
    # Use the full path to ensure it finds the file
    path = r'D:\DATA ANALYST BOOTCAMP\Loan Dashboard\data\loans.csv'
    return pd.read_csv(path)

df = load_data()

# ---- Sidebar ----
st.sidebar.title("🔍 Filter Panel")
branch_filter = st.sidebar.multiselect("Branch",
    df['branch'].unique(), default=list(df['branch'].unique()))
type_filter = st.sidebar.multiselect("Loan Type",
    df['loan_type'].unique(), default=list(df['loan_type'].unique()))
status_filter = st.sidebar.multiselect("Loan Status",
    df['status'].unique(), default=list(df['status'].unique()))

filtered_df = df[
    df['branch'].isin(branch_filter) &
    df['loan_type'].isin(type_filter) &
    df['status'].isin(status_filter)
]

# ---- Header ----
st.title("💰 Loan Portfolio Analytics Dashboard")
st.caption("Gold Loan NBFC — Operational Intelligence Platform")
st.markdown("---")

# ---- KPI Cards ----
kpis = get_kpis(filtered_df)
cols = st.columns(6)
for col, (key, val) in zip(cols, kpis.items()):
    col.metric(label=key, value=val)

st.markdown("---")

# ---- Row 1 ----
c1, c2 = st.columns(2)
with c1:
    st.subheader("📈 Monthly Disbursement Trend")
    monthly = monthly_disbursement(filtered_df)
    fig = px.line(monthly, x='month', y='loan_amount', markers=True,
                  labels={'loan_amount': 'Amount (₹)', 'month': 'Month'},
                  color_discrete_sequence=['#1f77b4'])
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("🟢 Loan Status Distribution")
    status_dist = loan_status_distribution(filtered_df)
    fig2 = px.pie(status_dist, names='status', values='count',
                  color_discrete_sequence=px.colors.qualitative.Set2,
                  hole=0.35)
    st.plotly_chart(fig2, use_container_width=True)

# ---- Row 2 ----
c3, c4 = st.columns(2)
with c3:
    st.subheader("🏢 Branch-wise Loan Volume")
    branch = branch_performance(filtered_df)
    fig3 = px.bar(branch, x='branch', y='total_amount', color='branch',
                  text_auto='.2s',
                  labels={'total_amount': 'Total Amount (₹)'},
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    st.subheader("🏅 Loan Type Breakdown")
    lt = loan_type_breakdown(filtered_df)
    fig4 = px.bar(lt, x='loan_type', y='loan_amount', color='loan_type',
                  text_auto='.2s',
                  labels={'loan_amount': 'Amount (₹)', 'loan_type': 'Type'})
    st.plotly_chart(fig4, use_container_width=True)

# ---- Row 3 ----
c5, c6 = st.columns(2)
with c5:
    st.subheader("📊 Credit Score Distribution")
    fig5 = px.histogram(filtered_df, x='credit_score', nbins=30,
                        color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig5, use_container_width=True)

with c6:
    st.subheader("🏦 NPA by Branch")
    branch_data = branch_performance(filtered_df)
    fig6 = px.bar(branch_data, x='branch', y='npa_count', color='branch',
                  text_auto=True,
                  labels={'npa_count': 'NPA Count'},
                  color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig6, use_container_width=True)

# ---- Raw Data ----
st.markdown("---")
with st.expander("📋 View Raw Loan Data"):
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

st.caption("Built by Preeti Ranjan Pradhan | Loan Portfolio Analytics | 2025")