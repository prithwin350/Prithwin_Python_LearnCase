from invoice_formatter import get_input, ReturnToMenu
import re

def clean_text(text):
    return " ".join(text.split())
    

def convert_to_slug(text):
    cleaned_text = clean_text(text)
    cleaned_text = cleaned_text.replace("-", " ")
    words = cleaned_text.lower().split()
    slug = "-".join(words)

    return slug

def convert_to_lowercase(text):
    return text.lower()

def find_and_replace(text, find_text, replacement_text):
    return re.sub(re.escape(find_text), replacement_text, text, flags=re.IGNORECASE)

def generate_initials(text):
    words = clean_text(text).split()
    initials = ""

    for word in words:
        initials += word[0].upper()

        if len(initials) == 3:
            break

    return initials

def find_and_replace_utility():
    try:
        text = get_input("Enter text (or 'exit' to return): ")
        find_text = get_input("Enter text to find (or 'exit' to return): ")
        replacement_text = get_input("Enter replacement text (or 'exit' to return): ")

        result = find_and_replace(text, find_text, replacement_text)

        print(f"Updated text: {result}")

    except ReturnToMenu:
        return

def text_utility(function, result_name):
    try:
        text = get_input("Enter text (or 'exit' to return): ")
        result = function(text)

        print(f"{result_name}: {result}")

    except ReturnToMenu:
        return

def text_manager():
    while True:
        print("\n========== Text Manager ==========")
        print("1. Clean Text")
        print("2. Convert to Slug")
        print("3. Convert to Lowercase")
        print("4. Find and Replace")
        print("5. Generate Initials")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text_utility(clean_text, "Cleaned text")
        elif choice == "2":
            text_utility(convert_to_slug, "Slug")
        elif choice == "3":
             text_utility(convert_to_lowercase, "Lowercase text")
        elif choice == "4":
            find_and_replace_utility()
        elif choice == "5":
            text_utility(generate_initials, "Initials")
        elif choice == "6":
            print("Text Manager closed.")
            break
        else:
            print("Invalid choice.")
def main():
    print("Text manager application has started")
    text_manager()

if __name__=="__main__":
    main()