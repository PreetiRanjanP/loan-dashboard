import pandas as pd

def monthly_disbursement(df):
    return df.groupby('month')['loan_amount'].sum().reset_index()

def branch_performance(df):
    return df.groupby('branch').agg(
        total_loans   = ('loan_id', 'count'),
        total_amount  = ('loan_amount', 'sum'),
        avg_credit    = ('credit_score', 'mean'),
        npa_count     = ('status', lambda x: (x == 'NPA').sum())
    ).reset_index()

def loan_status_distribution(df):
    return df['status'].value_counts().reset_index()

# THIS IS THE MISSING FUNCTION CAUSING YOUR ERROR:
def loan_type_breakdown(df):
    return df.groupby('loan_type')['loan_amount'].sum().reset_index()