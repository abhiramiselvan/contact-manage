import json

def add_contact(contacts, name, number):
    contacts[name] = number

def search_contact(contacts, name):
    if name in contacts:
        return f"Name: {name}, Number: {contacts[name]}"
    else:
        return "Contact not found."

print("Welcome to your Contact Management System!")

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

while True:
    print("\nPlease select your requirement. Would you like to create a new contact or search for an existing one?")
    print("a. Add a new contact")
    print("b. Search for a contact")
    print("c. Close this program")

    choice = input("Enter your option: ")

    if choice == "a":
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        add_contact(contacts, name, number)
        print(f"Contact for {name} added successfully.")

    elif choice == "b":
        name = input("Enter the name to search: ")
        result = search_contact(contacts, name)
        print(result)

    elif choice == "c":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")