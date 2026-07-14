import os

def get_existing_filename():
    filename = get_filename()

    if not os.path.exists(filename):
        print(f"{filename} doesn't exist.")
        return None

    return filename

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def create_file():
    filename = get_filename()

    if os.path.exists(filename):
        print(f"{filename} already exists.")
        return

    content = input("Enter file content: ")

    with open(filename, "w") as file:
        file.write(content)

    print(f"{filename} created successfully.")

def view_file():
    filename = get_existing_filename()

    if filename is None:
        return

    content = read_file(filename)

    print(f"\n========== {filename} ==========")
    print(content)

def edit_file():
    filename = get_existing_filename()

    if filename is None:
        return
    content = read_file(filename)

    old_text = input("Enter text to replace: ")
    new_text = input("Enter replacement text: ")

    content = content.replace(old_text, new_text)

    with open(filename, "w") as file:
        file.write(content)

def delete_file():
    filename = get_existing_filename()

    if filename is None:
        return

    os.remove(filename)

    print(f"{filename} deleted successfully.")

def get_filename():
    filename = input("Enter the file name without .txt: ").strip()

    if not filename.endswith(".txt"):
        filename += ".txt"

    return filename

def application():
    while True:
        print("\n========== File Manager ==========")
        print("1. Create File")
        print("2. View File")
        print("3. Edit File")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            view_file()
        elif choice == "3":
            edit_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("File Manager closed.")
            break
        else:
            print("Invalid choice.")


def main():
    application()


if __name__ == "__main__":
    main()