import sqlite3

# 1. Define the path, but don't open the connection yet
DB_PATH = r'C:\database\databaseoject.db'

# 2. Create a helper function to grab a fresh connection when needed
def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()       # Open fresh connection
    cursor = conn.cursor()
    
    query="""CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        department TEXT,
        salery REAL,
        joining_date TEXT
    )"""
    cursor.execute(query)
    conn.commit()
    
    cursor.close()
    conn.close()                  # Close it safely

def add_emp(first_name, last_name, department, salary, joining_date):
    conn = get_connection()
    cursor = conn.cursor()
    
    query="""INSERT INTO employee(first_name, last_name, department, salery, joining_date) VALUES(?,?,?,?,?)"""
    cursor.execute(query, (first_name, last_name, department, salary, joining_date))
    conn.commit()
    print(f"✅ Employee added successfully: {first_name} {last_name}")
    
    cursor.close()
    conn.close()

def view_emp():
    conn = get_connection()
    cursor = conn.cursor()
    
    query="""SELECT * FROM employee"""
    cursor.execute(query)
    records = cursor.fetchall()
    
    if not records:
        print("No employees found.")
    else:
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Dept: {row[3]} | Salary: ${row[4]}")
        
    cursor.close()
    conn.close()

def update_emp(emp_id, first_name, last_name, department, salery, joining_date):
    conn = get_connection()
    cursor = conn.cursor()
    
    query="""UPDATE employee SET first_name=?, last_name=?, department=?, salery=?, joining_date=? WHERE id=?"""
    cursor.execute(query, (first_name, last_name, department, salery, joining_date, emp_id))
    conn.commit()
    print(f"🔄 Employee updated successfully with ID {emp_id}")
    
    cursor.close()
    conn.close()

def delete_emp(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    query="""DELETE FROM employee WHERE id=?"""
    cursor.execute(query, (emp_id,))
    conn.commit()
    print(f"❌ Employee deleted successfully with ID {emp_id}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table() # Only need to call this once

    # The while loop is now properly indented under the __main__ block
    while True:
        print("\n" + "=" * 50)
        print("\tEMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("""
1. Add Employee
2. View Employees
3. Update Employee
4. Delete Employee
5. Exit
""")
        
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                department = input("Enter Department: ")
                salery = float(input("Enter Salary: "))
                joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
                add_emp(first_name, last_name, department, salery, joining_date)

            elif choice == 2:
                view_emp()

            elif choice == 3:
                emp_id = int(input("Enter Employee ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                department = input("Enter Department: ")
                salery = float(input("Enter Salary: "))
                joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
                update_emp(emp_id, first_name, last_name, department, salery, joining_date)

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to delete: "))
                delete_emp(emp_id)

            elif choice == 5:
                print("Thank you! Exiting...")
                break

            else:
                print("Invalid Choice. Please try again.")
                
        except ValueError:
            print("⚠️ Invalid input! Please enter numbers where required (like ID, Choice, or Salary).")