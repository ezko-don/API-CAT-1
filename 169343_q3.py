class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated Salary for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary}")

    def display_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()


def main():
    department_name = input("Enter department name: ")
    department = Department(department_name)

    while True:
        name = input("Enter employee name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter employee salary: "))
        employee = Employee(name, employee_id, salary)

        department.add_employee(employee)

    department.display_employees()
    department.calculate_total_salary()


if __name__ == "__main__":
    main()