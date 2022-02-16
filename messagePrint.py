def msgPrint(message):
    count=0
    while count<len(message):
        print(message[count])
        count=count+1

message=input("Enter a message: ")
msgPrint(message)