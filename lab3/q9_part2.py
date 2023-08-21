def recursive_binary_search(list,n):
    if len(list)==0:
        return False
    else:
        mid=len(list)//2
        if list[mid]==n:
            return True
        else:
            if n<list[mid]:
                return recursive_binary_search(list[:mid],n)
            else:
                return recursive_binary_search(list[mid+1:],n)

list=[]
x=int(input("Enter the number of elements : "))
for i in range(0,x):
    ele=int(input("Enter the element : "))
    list.append(ele)
list.sort()
n=int(input("Enter the number to be searched : "))
print(recursive_binary_search(list,n))