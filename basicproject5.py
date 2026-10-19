#library mangement system
books=[]
def add_book():
    book_id=int(input("enter book id"))
    book_name=input("enter book name:")
    author=input("enter author name:")
    book=[book_id,book_name,author,"available"]
    books.append(book)
    print("book added successfully")
def display_book():
    if len(books)==0:
        print("no books added")
    else:
        for book in books:
            print(book)
def search_book():
    book_id = int(input("Enter book id to search: "))

    for book in books:
        if book[0] == book_id:
            print("Book details:", book)
            return

    print("Book not found")
def issue_book():
    book_id = int(input("Enter book id to issue: "))

    for book in books:
        if book[0] == book_id:
            if book[3] == "available":
                book[3] = "issued"
                print("Book issued successfully")
            else:
                print("Book is already issued")
            return

    print("Book not found")
def return_book():
    book_id = int(input("Enter book id to return: "))

    for book in books:
        if book[0] == book_id:
            if book[3] == "issued":
                book[3] = "available"
                print("Book returned successfully")
            else:
                print("Book was not issued")
            return

    print("Book not found")
while True:
    print("\n---Library Management System---")
    print("1. add book")
    print("2. display book")
    print("3. search book")
    print("4. issue book")
    print("5. return book")
    print("6. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you")
        break
    else:
        print("Invalid choice number")

            
    
