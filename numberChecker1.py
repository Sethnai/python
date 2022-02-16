no=int(input("Please Enter your Number: "))

if no>1000:
    print("A")
    if no>2000:
        print("C")
    else:
        print("D")
    print("H")
else:
    print("B")
    if no>500:
        print("E")
    else:
        print("F")
    print("G")
print("I")