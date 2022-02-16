def wordCount(msg):
    space=0
    i=0
    while i<len(msg):
        if msg[i]==" ":
            space=space+1
        i=i+1
    print("In this message there are ",space+1,"words")

msg=input("Type in your document: \n")
wordCount(msg)