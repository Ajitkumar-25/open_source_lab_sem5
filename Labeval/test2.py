cart={
    "pen":35,
    "pencil":10,
    "eraser":5,
    "sharpner":5,
    "scale":10,
    "notebook":40,
    "register":20,
    "book":50,
    "bag":100,
    "lunchbox":50,
    "waterbottle":50
}

print("Welcome to stationery shop We have Following options ")
print("1. Add an item")
print("2. total cost after offering dicount")
print("3. Display all items")
print("4. Exit")

while(True):
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=input("Enter the name of the item: ")
        price=int(input("Enter the price of the item: "))
        cart[item]=price
    elif choice==2:
        total=0
        for item,price in cart.items():
            total+=price
        if total>1000:
            total=total-total*0.1
        print("Total cost after discount is: ",total)
    elif choice==3:
        for item,price in cart.items():
            print(item," by ",price)
    elif choice==4:
        break
    else:
        print("Invalid choice")

3       