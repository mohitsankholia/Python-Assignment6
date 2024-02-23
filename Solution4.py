dict1 = {0: 10, 1: 20}

keys = dict1.keys()
checkKey = int(input("Enter key : "))

if checkKey in keys:
    print("present")
else:
    print("not present")