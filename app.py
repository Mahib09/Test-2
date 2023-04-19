def menu():
    print("""
Menu

1. Add a record

2. Search a record

3. Change a record

4. Delete a record

5. Quit
        """)
phonedirectory={}
print("""
WELCOME TO THE GRANN'S PHONE DIRECTORY

1. Add a record

2. Search a record

3. Update a record

4. Delete a record

5. Quit
""")

option=int(input("Enter Your Choice: "))

while option!=5:
    if option==1:
        name=input("Enter Name: ")
        phonenumber=int(input("Enter your 10-digit phone number: "))
        if phonenumber>9999999999 and phonenumber<999999999:
            print("Invalid Number")
        else:
            phonedirectory[name]=phonenumber
            print("Record Added")
        menu()
    elif option==2:
        name=input("Enter name to Search: ")
        if name in phonedirectory:
            print(name, ":" ,phonedirectory[name])
        else:
            print("No phonenumber exists with this name")
        menu()
    elif option==3:
        name=input("Enter Name: ")
        phonenumber=input("Enter new 10-digit phone number: ")
        phonedirectory[name]=phonenumber
        print("Record Updated")
        menu()
    elif option==4:
        name=input("Enter name: ")
        del(phonedirectory[name])
        print("Record Deleted")
        menu()
    elif option!=5:
        print("Invalid Option")
        menu()
    option=int(input("Enter Your Choice: "))
else:
    print("Program Closed")