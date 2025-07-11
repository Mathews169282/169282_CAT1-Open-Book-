class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary updated to {self.salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name}")

    def total_salary_expenditure(self):
        total = sum(e.salary for e in self.employees)
        print(f"Total salary expenditure: {total}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name}:")
        for e in self.employees:
            e.display_details()

# Interactive system
if __name__ == "__main__":
    dept = Department("IT Department")

    while True:
        print("\n1. Add Employee\n2. Show Employees\n3. Update Salary\n4. Show Total Salary\n5. Exit")
        choice = input("Select: ")

        if choice == "1":
            name = input("Employee Name: ")
            eid = input("Employee ID: ")
            salary = float(input("Salary: "))
            emp = Employee(name, eid, salary)
            dept.add_employee(emp)

        elif choice == "2":
            dept.display_all_employees()

        elif choice == "3":
            eid = input("Employee ID to update: ")
            for e in dept.employees:
                if e.employee_id == eid:
                    new_salary = float(input("New Salary: "))
                    e.update_salary(new_salary)
                    break
            else:
                print("Employee not found.")

        elif choice == "4":
            dept.total_salary_expenditure()

        elif choice == "5":
            break
