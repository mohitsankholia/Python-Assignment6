dict1 = {1: 10, 8: 20, 6: 30, 4: 40, 3: 50, 9: 60}

sortDict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

maxThreeValues = sortDict[:3]

maxThreeValuesDict = dict(maxThreeValues)

print(maxThreeValuesDict)