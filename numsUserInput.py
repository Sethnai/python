nums=[]
choice="Y"
while choice=="Y" or choice=="y":
    no=int(input("Enter any number: "))
    nums.append(no)
    choice=input("Do you want to enter another number? (Y/N) ")

print("You have entered", len(nums)," values")