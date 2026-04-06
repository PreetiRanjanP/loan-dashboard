import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Create the folder if it doesn't exist
folder = r"D:\DATA ANALYST BOOTCAMP\Loan Dashboard\data"
if not os.path.exists(folder):
    os.makedirs(folder)

fake = Faker('en_IN')
np.random.seed(42)
n = 1000

data = {
    'loan_id': [f'LN{str(i).zfill(5)}' for i in range(1, n+1)],
    'customer_name': [fake.name() for _ in range(n)],
    'branch': [random.choice(['Bhubaneswar', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai']) for _ in range(n)],
    'loan_type': [random.choice(['Gold Loan', 'Personal Loan', 'Business Loan']) for _ in range(n)],
    'loan_amount': np.random.randint(50000, 1500000, n),
    'interest_rate': np.round(np.random.uniform(8.5, 18.0, n), 2),
    'tenure_months': np.random.choice([6, 12, 18, 24, 36], n),
    'disbursed_date': pd.date_range('2023-01-01', periods=n, freq='8h').date,
    'status': random.choices(['Active', 'Closed', 'Defaulted', 'NPA'], weights=[50, 30, 12, 8], k=n),
    'emi_amount': np.random.randint(3000, 50000, n),
    'repaid_amount': np.random.randint(0, 1500000, n),
    'credit_score': np.random.randint(550, 850, n),
}

df = pd.DataFrame(data)
df['month'] = pd.to_datetime(df['disbursed_date']).dt.to_period('M').astype(str)

# SAVE TO ABSOLUTE PATH
path = os.path.join(folder, "loans.csv")
df.to_csv(path, index=False)
print(f"✅ SUCCESS: File saved at {path}")