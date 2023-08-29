books={
    "the alchemist":"Paulo Coelho",
    "the monk who sold his ferrari":"Robin Sharma",
    "the power of your subconscious mind":"Joseph Murphy",
    "the power of now":"Eckhart Tolle"
}
print("Welcome to library We have Following options ")
print("1. Add a book")
print("2. Delete a book")
print("3. Display all books")
print("4. Exit")

while(True):
    choice=int(input("Enter your choice: "))
    if choice==1:
        book=input("Enter the name of the book: ")
        author=input("Enter the name of the author: ")
        books[book]=author
    elif choice==2:
        book=input("Enter the name of the book: ")
        if book in books:
            del books[book]
        else:
            print("Book not found")
    elif choice==3:
        for book,author in books.items():
            print(book," by ",author)
    elif choice==4:
        break
    else:
        print("Invalid choice")



print("Thanks for using our library")

