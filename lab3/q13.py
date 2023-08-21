import re
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow(.com)"]
print("orignal string : ",items)
print("\nAfter removing parenthesis : ")
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))
	