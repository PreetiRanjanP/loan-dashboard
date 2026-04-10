import sys
import os
import pandas as pd

# 1. Dynamic Pathing (Works on both your Windows PC and Cloud Linux)
# This finds the 'Loan Dashboard' root folder regardless of where the script is run from.
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# 2. Robust Import
try:
    from db.db_connect import get_connection
except ImportError:
    print("❌ Error: Could not find 'db_connect.py' in the 'db' folder.")
    sys.exit(1)

# 3. Optimized Logic
def load_to_mysql():
    conn = None
    try:
        # Construct absolute path to the CSV to avoid FileNotFoundError
        csv_path = os.path.join(root_path, 'data', 'loans.csv')
        
        if not os.path.exists(csv_path):
            print(f"❌ Error: {csv_path} not found. Please run your data generation script first.")
            return

        df = pd.read_csv(csv_path)
        
        # Connect to MySQL
        conn = get_connection()
        if not conn:
            return
            
        cursor = conn.cursor()

        # Create Table if not exists (Professional addition)
        # Adjust column names/types based on your actual loans.csv structure
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                loan_id VARCHAR(50) PRIMARY KEY,
                customer_name VARCHAR(255),
                loan_amount FLOAT,
                loan_type VARCHAR(50),
                status VARCHAR(50),
                branch VARCHAR(100),
                credit_score INT,
                month VARCHAR(20),
                disbursement_date DATE,
                repayment_date DATE,
                interest_rate FLOAT,
                tenure INT,
                npa_status VARCHAR(10)
            )
        """)

        # Efficient Insertion using execute_many (Faster than a for-loop)
        # Using REPLACE or INSERT IGNORE depending on your preference
        sql = """INSERT IGNORE INTO loans VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        # Convert dataframe to list of tuples
        data_to_insert = [tuple(x) for x in df.values]
        
        cursor.executemany(sql, data_to_insert)
        
        conn.commit()
        print(f"✅ Success! {cursor.rowcount} rows processed and loaded into MySQL.")
        cursor.close()

    except Exception as e:
        print(f"❌ Database Error: {e}")
        print("💡 Hint: If deploying to Cloud, ensure your DB Host is public (not localhost).")
    
    finally:
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    load_to_mysql()