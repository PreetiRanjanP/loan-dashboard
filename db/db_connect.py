import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Preeti@003",   # ← replace this
        database="loan_analytics"
    )