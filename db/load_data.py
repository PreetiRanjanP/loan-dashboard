import sys
import os
import pandas as pd

# 1. Add the root folder to the path so it can find the 'db' folder
sys.path.append(os.getcwd())

# 2. Try to import the connection function
try:
    from db.db_connect import get_connection
except ImportError:
    print("❌ Error: Could not find 'db_connect.py' in the 'db' folder.")
    sys.exit(1)

# 3. Main Logic
def load_to_mysql():
    conn = None
    try:
        # Load the CSV
        csv_path = os.path.join('data', 'loans.csv')
        if not os.path.exists(csv_path):
            print(f"❌ Error: {csv_path} not found. Run generate_data.py first.")
            return

        df = pd.read_csv(csv_path)
        
        # Connect to MySQL
        conn = get_connection()
        cursor = conn.cursor()

        inserted = 0
        for _, row in df.iterrows():
            try:
                cursor.execute("""
                    INSERT IGNORE INTO loans VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, tuple(row))
                inserted += 1
            except Exception as e:
                print(f"⚠️ Skipping row due to error: {e}")

        conn.commit()
        print(f"✅ Success! {inserted} rows processed and loaded into MySQL.")
        cursor.close()

    except Exception as e:
        print(f"❌ Database Error: {e}")
        print("💡 Hint: Check your MySQL password in db/db_connect.py")
    
    finally:
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    load_to_mysql()