def salarySlip(name,salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    netSalary=salary-tax
    print("Name of Employee: ",name)
    print("Salary: £",salary)
    print("Tax: £",tax)
    print("Net Salary: £",netSalary,"\n")

salarySlip("James",2000)
salarySlip("Peter",5000)