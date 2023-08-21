def iterative_binary_search(list,n):
    first=0
    last=len(list)-1
    found=False
    while(first<=last and not found):
        mid=(first+last)//2
        if(list[mid]==n):
            found=True
            print("Element found at position",mid+1)
        else:
            if(n<list[mid]):
                last=mid-1
            else:
                first=mid+1
    if(found==False):
        print("Element not found")

list=[]
x=int(input("Enter the number of elements : "))
for i in range(0,x):
    ele=int(input("Enter the element : "))
    list.append(ele)
list.sort()
n=int(input("Enter the number to be searched : "))
iterative_binary_search(list,n)