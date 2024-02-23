number = int(input("Enter number : "))
dict1 = {}

for num in range(1, number + 1):
    dict1.update({num: num * num})

print(dict1)