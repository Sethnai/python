quantity = 90
price = 8
bill = quantity * price
vat = bill*20/100
print("Quantity: ",quantity)
print("Unit Price: ",price)
print("-----------------------")
print("Your bill is: £",bill)
print("You have to pay: £",vat,"as vat")
print("Your total bill is: £",bill + vat)
print("-----------------------")