def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
list=[1,2,4,5,4,5,6,9,10]
print("Orignal List is : ",end="")
print(list)   
print()
print('New List with unique elements is : ',end="")
print(unique_list(list))
print()