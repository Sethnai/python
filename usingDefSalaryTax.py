def tax(salary):
    t=salary*20/100
    return t

salary=int(input("What is the salary: £"))
netSalary=salary-tax(salary)
print("Tax: £",tax(salary))
print("Net: £",netSalary)