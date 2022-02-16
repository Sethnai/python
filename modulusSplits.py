no=int(input("enter a 2 digit number: "))

print(int(no/10)+(no%10))

no=int(input("enter a 3 digit number: "))

print(int(no/100)+int((no/10)%10)+(no%10))

print(int(no/100)+int(no%100/10)+(no%10))