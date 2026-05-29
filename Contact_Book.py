# Contact Book Management System

contacts = []


# Function to add contact
def add_contact():

    print("\n===== ADD CONTACT =====")

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("✅ Contact Added Successfully!")


# Function to view contacts
def view_contacts():

    print("\n===== CONTACT LIST =====")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):

        print(f"\nContact {index}")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")


# Function to search contact
def search_contact():

    print("\n===== SEARCH CONTACT =====")

    search = input("Enter name or phone number: ").lower()

    found = False

    for contact in contacts:

        if (search == contact['name'].lower() or
                search == contact['phone']):

            print("\n✅ Contact Found!")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")

            found = True

    if not found:
        print("❌ Contact not found.")


# Function to update contact
def update_contact():

    print("\n===== UPDATE CONTACT =====")

    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:

        if contact['phone'] == phone:

            print("\nEnter New Details")

            contact['name'] = input("New Name: ")
            contact['phone'] = input("New Phone: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")

            print("✅ Contact Updated Successfully!")
            return

    print("❌ Contact not found.")


# Function to delete contact
def delete_contact():

    print("\n===== DELETE CONTACT =====")

    phone = input("Enter phone number of contact to delete: ")

    for contact in contacts:

        if contact['phone'] == phone:

            contacts.remove(contact)

            print("✅ Contact Deleted Successfully!")
            return

    print("❌ Contact not found.")


# Main menu
while True:

    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\n🙏 Exiting Contact Book...")
        break

    else:
        print("❌ Invalid Choice! Please try again.")