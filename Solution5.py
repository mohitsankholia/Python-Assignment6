dict1 = {"name": "mohit",
         "surname": "sankholia",
         "addrress": "bengalure",
         "country": "india"}

keyValues = dict1.keys()

for val in keyValues:
    print(val, " : ", dict1.get(val))
