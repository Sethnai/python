bill=int(input("Payment Due: £"))
paid=int(input("Amount Paid: £"))
change=paid-bill
print("Change due: £",change)

count = 0
denomination= [50,20,10,5,2,1]
while count<len(denomination):
    if change>=denomination[count]:
        changeQuantity=int(change/denomination[count])
        print("£",denomination[count],": ",changeQuantity)
        change=change-(changeQuantity*denomination[count])
        count=count+1
    else:
        count=count+1

print("Have a nice day")