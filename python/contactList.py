class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def view_contacts(self):
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

def main():
    contact_list = ContactList()

    while True:
        print("\n1: Add Contact")
        print("2: View Contacts")
        print("3: Delete Contact")
        print("4: Exit")

        choice = int(input("\nSelect an option: "))

        if choice == 1:
            name = input("\nEnter Contact Name: ")
            phone = input("Enter Phone Number: ")
            contact_list.add_contact(name, phone)
        elif choice == 2:
            contact_list.view_contacts()
        elif choice == 3:
            name = input("\nEnter Contact Name to Delete: ")
            contact_list.delete_contact(name)
        elif choice == 4:
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
