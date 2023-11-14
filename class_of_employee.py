class Employee:
    def __init__ (self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary    
employee_1=Employee(input("Enter the first name of first employee: "),input("Enter the last name of first employee: "),input("Enter the salary of first employee: "))
employee_2=Employee(input("Enter the first name of second employee: "),input("Enter the last name of second employee: "),input("Enter the salary of second employee: "))
print("The first name of employees are:"+employee_1.fname,employee_2.fname)
print("The full name and salary of employee_1: "+employee_1.fname,employee_1.lname,employee_1.salary)
print("The full name and salary of employee 2: "+employee_2.fname,employee_2.lname,employee_2.salary)
