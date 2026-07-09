student_names = ["John", "Alice", "Bob", "Sarah", "Mike"]
student_marks = [85, 73, 91, 64, 88]

def show_list():
    print("Current Students:")
    for i in range(len(student_names)):
        print(f"Name: {student_names[i]}  Mark: {student_marks[i]}")

def student_summary():
    print("Student Summary selected.")
    total_students= len(student_names)
    if total_students == 0:
        print("No students in the list.")
        return
    else:
        total = sum(student_marks)
        average = total / len(student_marks)
        highest_mark = max(student_marks)
        lowest_mark = min(student_marks)

        print("\nClass Summary:")
        print(f"Total Marks: {total}")
        print(f"Average Mark: {average:.2f}")
        print(f"Highest Mark: {highest_mark}")
        print(f"Lowest Mark: {lowest_mark}")

def update_student_mark():
    print("Update Student Mark selected.")
    while True:
        student_name = input("Enter the name of the student to update (or type 'done' to finish): ")

        if student_name.lower() == "done":
            break

        if student_name in student_names:
            index=student_names.index(student_name)
            try:
                new_mark= int(input(f"Enter the new mark for {student_name}: "))
                student_marks[index] = new_mark
                print(f"Updated {student_name}'s mark to {new_mark}.")
                show_list()
            except:
                print("Invalid mark. Please enter a valid integer.\n")
                continue
        else:
            print(f"Student '{student_name}' not found in the list.")

def remove_student():
    print("Remove Student selected.")
    student_name = input("Enter the name of the student to remove: ")

    if student_name in student_names:
        index = student_names.index(student_name)
        removed_name = student_names.pop(index)
        removed_mark = student_marks.pop(index)
        print(f"Removed {removed_name} with mark {removed_mark}.")
        show_list()
    else:
        print(f"Student '{student_name}' not found in the list.")

def add_student():
    while True:
        student_name = input("Enter student name (type 'done' to finish): ")

        if student_name.lower() == "done":
            break

        try:
            student_mark = int(input("Enter student mark: "))

            student_names.append(student_name)
            student_marks.append(student_mark)

            print("\nCurrent Students:")
            show_list()

        except ValueError:
            print("Invalid mark. Please enter a valid integer.\n")

def student_analyzer():
    while True:
        print("\n=====================================")
        print("      Student Marks Manager")
        print("=====================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Mark")
        print("4. Remove Student")
        print("5. Show Class Summary")
        print("6. Exit")
        print("=====================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_list()

        elif choice == "3":
            update_student_mark()

        elif choice == "4":
            remove_student()

        elif choice == "5":
            student_summary()

        elif choice == "6":
            print("Exiting Student Marks Manager...")
            break

        else:
            print("Invalid option. Please try again.")

def main():
    print("Welcome to the Student List Analyzer!")
    student_analyzer()

main()