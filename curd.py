import sqlite3

# Create a SQLite database and a table
conn = sqlite3.connect("crud.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")
conn.commit()

# Function to create a new record
def create_record(name, age):
    cursor.execute("INSERT INTO records (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Record created successfully.")

# Function to read all records
def read_records():
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")

# Function to update a record
def update_record(record_id, name, age):
    cursor.execute("UPDATE records SET name = ?, age = ? WHERE id = ?", (name, age, record_id))
    conn.commit()
    print("Record updated successfully.")

# Function to delete a record
def delete_record(record_id):
    cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
    print("Record deleted successfully.")

# Main program loop
while True:
    print("CRUD Operations Menu:")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        create_record(name, age)
    elif choice == '2':
        read_records()
    elif choice == '3':
        record_id = int(input("Enter the record ID to update: "))
        name = input("Enter the new name: ")
        age = int(input("Enter the new age: "))
        update_record(record_id, name, age)
    elif choice == '4':
        record_id = int(input("Enter the record ID to delete: "))
        delete_record(record_id)
    elif choice == '5':
        print("Exiting the program.")
        conn.close()
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

