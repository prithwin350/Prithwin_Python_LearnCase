# FOR REVIEWER:
# Run `test_file.py` before testing this application.
# It automatically creates the `test_folder` and sample files
# required to test the file organization features.

from pathlib import Path
import shutil

def get_input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")


def get_category(extension):
    extension = extension.lower()

    if extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
        return "Images"

    elif extension in [".mp4", ".avi", ".mov", ".mkv"]:
        return "Videos"

    elif extension in [".mp3", ".wav", ".flac"]:
        return "Audio"

    elif extension in [".pdf", ".docx", ".txt", ".xlsx", ".pptx"]:
        return "Documents"

    else:
        return "Others"


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved: {source.name} -> {destination.parent.name}")

    except FileNotFoundError:
        print("Source file not found.")

    except PermissionError:
        print("Permission denied.")

    except OSError as e:
        print(f"File operation failed: {e}")


def create_folder(foldername):
    folder=Path(foldername)
    folder.mkdir(exist_ok=True)
    print("Folder created")


def check_folder(folder_name):
    folder = Path(folder_name)

    if folder.is_dir():
        print("Folder exists.")
        return True
    else:
        print("Folder doesn't exist.")
        return False


def list_folder(folder_name):
    folder = Path(folder_name)

    if not check_folder(folder_name):
        return

    print("Checking folder...")

    try:
        for item in folder.iterdir():
            print(item)
    except PermissionError:
        print("Permission denied.")
    except OSError as e:
        print(f"Error accessing folder: {e}")


def organize_files(folder_name):
    folder = Path(folder_name)

    if not check_folder(folder_name):
        return

    for item in folder.iterdir():

        if item.is_file():
            category = get_category(item.suffix)

            destination_folder = folder / category

            create_folder(destination_folder)

            destination = destination_folder / item.name

            move_file(item, destination)

    print("Organization complete.")


def application():
    while True:
        print("\n=== File Organizer ===")
        print("1. Check if folder exists")
        print("2. Create folder")
        print("3. List folder contents")
        print("4. Check extension category")
        print("5. Move file")
        print("6. Organize folder")
        print("7. Exit")

        choice = get_input("Select an option: ", int)

        if choice == 1:
            folder_name = get_input("Enter folder name: ")
            check_folder(folder_name)

        elif choice == 2:
            folder_name = get_input("Enter folder name to create: ")
            create_folder(folder_name)

        elif choice == 3:
            folder_name = get_input("Enter folder name: ")
            list_folder(folder_name)

        elif choice == 4:
            extension = get_input("Enter file extension: ")
            print(get_category(extension))

        elif choice == 5:
            source = Path(get_input("Enter source file path: "))
            destination = Path(get_input("Enter destination file path: "))
            move_file(source, destination)

        elif choice == 6:
            folder_name = get_input("Enter folder to organize: ")
            organize_files(folder_name)

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


def main():
    print("=== File Organizer ===")
    application()


if __name__ == "__main__":
    main()