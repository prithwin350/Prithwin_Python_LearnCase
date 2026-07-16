import json
import os

data = {
    "contacts": []
}

#========================Utilities Functions starts here========================#
def get_input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except ValueError:
            print("Invalid input. Try again.")



def normalize_filename(filename):
    if not filename.endswith(".json"):
        filename += ".json"

    return filename


def check_file_exists(filename):
    return os.path.exists(filename)


def get_contact(filename):
    contact = {
        "contact_id": generate_contact_id(filename),
        "first_name": get_input("Enter First Name: "),
        "last_name": get_input("Enter Last Name: "),
        "phone_number": get_input("Enter Phone Number: "),
        "email": get_input("Enter Email: ")
    }

    return contact


def get_updated_contact():
    contact = {
        "first_name": get_input("Enter first name: "),
        "last_name": get_input("Enter last name: "),
        "phone_number": get_input("Enter phone number: "),
        "email": get_input("Enter email: ")
    }

    return contact


def generate_contact_id(filename):
    data = open_json_file(filename)

    if data is None:
        return None

    contacts = data["contacts"]

    if len(contacts) == 0:
        return "0001"

    last_id = int(contacts[-1]["contact_id"])

    new_id = last_id + 1

    return str(new_id).zfill(4)
#========================Utilities Functions ends here========================#


def create_json_file(filename):
    if check_file_exists(filename):
        print("Contact book already exists.")
        return

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("Contact book created successfully.")


def open_json_file(filename):
    if not check_file_exists(filename):
        print("File not found.")
        return None

    with open(filename, "r") as file:
        data=json.load(file)
        print(os.path.abspath(filename))
        print(f"Opening {filename}")
        return data


def delete_json_file(filename):
    if not check_file_exists(filename):
        print("File not found.")
        return

    os.remove(filename)
    print(f"{filename} deleted successfully.")


def add_contact(filename, contact):
    data = open_json_file(filename)

    if data is None:
        return
    
    data["contacts"].append(contact)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Contact added successfully to {filename}.")


def view_contacts(filename):
    data = open_json_file(filename)

    if data is None:
        return

    contacts = data["contacts"]

    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n===== Contacts =====")

    print("-" * 80)
    print(f"{'ID':<10}{'First Name':<15}{'Last Name':<15}{'Phone':<15}{'Email':<25}")
    print("-" * 80)

    for contact in contacts:
        print(
            f"{contact['contact_id']:<10}"
            f"{contact['first_name']:<15}"
            f"{contact['last_name']:<15}"
            f"{contact['phone_number']:<15}"
            f"{contact['email']:<25}"
        )

    print("-" * 80)


def delete_contact(filename, contact_id):
    data = open_json_file(filename)

    if data is None:
        return

    contacts=data["contacts"]

    found = False

    for contact in contacts:
        if contact["contact_id"]==contact_id:
            found = True
            contacts.remove(contact)
            break
    
    if not found:
        print("Contact not found.")
        return
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Contact deleted successfully on {filename}.")


def update_contact(filename, contact_id, updated_contact):
    data = open_json_file(filename)

    if data is None:
        return

    contacts = data["contacts"]

    for contact in contacts:
        if contact["contact_id"] == contact_id:

            contact.update(updated_contact)

            break

    else:
        print("Contact not found.")
        return

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Contact updated successfully in {filename}.")


def contact_book(filename):
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contacts")
        print("4. Update Contacts")
        print("5. Back")
        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                print("Add Contact")
                contact = get_contact(filename)
                add_contact(filename, contact)

            elif choice == "2":
                print("View Contacts")
                view_contacts(filename)

            elif choice == "3":
                print("Delete Contacts")
                contact_id=input("Enter your Contact ID: ")
                delete_contact(filename,contact_id)
            
            elif choice == "4":
                print("Update Contacts")
                contact_id = input("Enter your Contact ID: ")
                updated_values = get_updated_contact()
                update_contact(filename, contact_id,updated_values)

            elif choice == "5":
                break

            else:
                print("Invalid choice.")
        except Exception as error:
            print(f"Error adding contact: {error}")


def application():
    print("======= Welcome =======")

    while True:
        try:
            print("\n1. Create Contact Book")
            print("2. Open Contact Book")
            print("3. Delete Contact Book")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Create Contact Book")
                filename = normalize_filename(input("Enter filename: "))
                create_json_file(filename)

            elif choice == "2":
                print("Open Contact Book")
                filename = normalize_filename(input("Enter filename: "))

                data = open_json_file(filename)

                if data is not None:
                    contact_book(filename)
            
            elif choice == "3":
                filename = normalize_filename(input("Enter filename: "))
                delete_json_file(filename)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as error:
            print(f"Unexpected error: {error}")


def main():
    print("Application started")

    try:
        application()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")


if __name__ == "__main__":
    main()