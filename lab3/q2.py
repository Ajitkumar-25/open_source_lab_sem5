def valuesort(myDict):
    print("Dictionary before sorting:")
    for key in myDict:
           print(key, ":", myDict[key])
    print()
    myKeys = list(myDict.keys())
    myKeys.sort()
    sorted_dict = {i: myDict[i] for i in myKeys}
    print("Dictionary after sorting based on keys:")
    for key in sorted_dict:
            print(key, ":", myDict[key])

myDict={'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}
valuesort(myDict)