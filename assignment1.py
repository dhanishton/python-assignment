#Dhaniston R

import sys

contacts = { }

def menu():
    print("*****************  MENU  *******************")
    print("press 1 to add a new contact to the contact book.")
    print("press 2 to display all contacts")
    print("press 3 to delete an existing contact")
    print("press 4 if you want to Exit Contact Book.")
    
    print("press any number from 6-9 to display Menu")
    print("----------------------------------------------")
    print("            CONTACT BOOK              ")
menu()
def display():
    for key, value1 in contacts.items():
        print(key, ":", value1)

def checkAlreadyExist(number,email):
    for value1 in contacts.values():
        if number in value1:
            return 1
        if email in value1:
            return 2    
    return 0

def displayLastUpdatedPerson(name):
    lastPerson=contacts.get(name)
    print(name, ":",lastPerson)    
while True:

    try:
        choice = int(input("Please enter your choice:"))
        
        if choice == 1:
            Name = input("Enter Name:").upper()
            Number = (input("Enter 10 digit mobile number: "))
            Email = input("Enter e-mail address:")
            if checkAlreadyExist(Number,Email)==1:
                print("Number already exist")
            elif checkAlreadyExist(Number,Email)==2:
                print("Email already exist")  

            else  :
                if len(Number) == 10:
                    contacts.update({Name:["Number",Number,"Email",Email]})
                    print("              CONTACT")
                    displayLastUpdatedPerson(Name)
                else:
                    print("Number is invalid.Please try again.")

       
        elif choice == 3:
            delete = input("Please enter the name of the contact you wish to remove:")
            del contacts[delete]
            print("              CONTACTS")
            display()
        elif choice == 4:
            print("Thank you for using the Contact Book!")
            break
        elif choice == 2:
            print("              CONTACTS")
            display()
        else:
            menu()
    except :
       
       
        print("Invalid Command") 
          
    