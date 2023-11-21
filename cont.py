import json

def add_contact(contacts, name, number, text_file):
    contacts[name] = number
    with open(text_file, "a") as file:
        file.write(f"{name}: {number}\n")

def search_contact(name, text_file):
    with open(text_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if name in line:
                return line
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
        add_contact(contacts, name, number, "ContacDiary.txt")
        print(f"Contact for {name} added successfully.")
        

    elif choice == "b":
        name = input("Enter the name to search: ")
        result = search_contact(name, "ContacDiary.txt")
        print(result)
        

    elif choice == "c":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")