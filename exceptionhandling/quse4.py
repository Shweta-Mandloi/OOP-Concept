import sqlite3

try:
    # Database connection
    conn = sqlite3.connect("student.db")  # agar file nahi mili to ye create ho jayegi
    cursor = conn.cursor()

    # Table create
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")

    # Data insert
    cursor.execute("INSERT INTO students (name) VALUES (?)", ("Shweta",))
    conn.commit()

    print("✅ Database connected & data inserted successfully!")

except sqlite3.Error as e:
    print("❌ Database error:", e)

finally:
    if conn:
        conn.close()
        print("🔔 Database connection closed.")
