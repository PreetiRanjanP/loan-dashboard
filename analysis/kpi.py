def get_kpis(df):
    total_loans = len(df)
    total_aum = df['loan_amount'].sum()
    avg_ticket = df['loan_amount'].mean()
    npa_rate = (df['status'] == 'NPA').mean() * 100
    collection_eff = (df['repaid_amount'].sum() / df['loan_amount'].sum()) * 100

    return {
        'Total Loans': total_loans,
        'Total AUM (₹)': f"₹{total_aum:,.0f}",
        'Avg Ticket Size (₹)': f"₹{avg_ticket:,.0f}",
        'NPA Rate (%)': f"{npa_rate:.2f}%",
        'Collection Efficiency': f"{collection_eff:.2f}%"
    }