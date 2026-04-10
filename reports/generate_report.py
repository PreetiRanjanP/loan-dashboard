import sys
sys.path.insert(0, 'D:\\DATA ANALYST BOOTCAMP\\PROJECTS_OWN\\Loan Dashboard')

import pandas as pd
from analysis.kpi import get_kpis
from analysis.trends import (branch_performance, loan_status_distribution,
                              loan_type_breakdown, monthly_disbursement)

df = pd.read_csv('data/loans.csv')

with pd.ExcelWriter('reports/Loan_Report.xlsx', engine='openpyxl') as writer:
    pd.DataFrame(get_kpis(df).items(),
        columns=['KPI', 'Value']).to_excel(writer, sheet_name='KPIs', index=False)
    branch_performance(df).to_excel(writer, sheet_name='Branch Performance', index=False)
    loan_status_distribution(df).to_excel(writer, sheet_name='Loan Status', index=False)
    loan_type_breakdown(df).to_excel(writer, sheet_name='Loan Type', index=False)
    monthly_disbursement(df).to_excel(writer, sheet_name='Monthly Trend', index=False)
    df.to_excel(writer, sheet_name='Raw Data', index=False)

print("✅ Report saved → reports/Loan_Report.xlsx")