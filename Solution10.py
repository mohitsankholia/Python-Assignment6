dict1 = {'a': 2, 'b': 2, 'c': 2}

dictKey = dict1.keys()
popKey = input("Enter key : ")

if popKey in dictKey:
    dict1.pop(popKey)
    print(dict1)
else:
    print("key not found")