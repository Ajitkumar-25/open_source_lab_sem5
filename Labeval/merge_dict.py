# Python code to merge dict using update() method
def Merge(dict1, dict2):
	return(dict2.update(dict1))


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This returns None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)



# code
# Python code to merge dictionary
def Merge(dict1, dict2):
	for i in dict2.keys():
		dict1[i]=dict2[i]
	return dict1
	
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

# This code is contributed by Bhavya Koganti
