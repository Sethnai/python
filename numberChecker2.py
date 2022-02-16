no=int(input("Please Enter your Number: "))

if no>1000:
    print("A")
    if no>2000:
        print("C")
        if no>3000:
            print("H")
        print("M")
    else:
        print("D")
        if no>1500:
            print("J")
        else:
            print("I")
        print("L")
    print("N")
else:
    print("B")
    if no>500:
        print("E")
    else:
        print("F")
    print("K")
print("O")
print("P")