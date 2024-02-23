d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 2, 'key2': 9}

for keys in d1.keys():
    if keys in d2.keys() and d1.get(keys) == d2.get(keys):
        print("same key value present as", keys, ":", d1.get(keys))