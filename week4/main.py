from config.database import check_connection
from database.migrations import create_tables
from ui.menu import ui


def application():
    print("Welcome to DEIENAMI")

    if check_connection():
        print("Database connection successful.")
    else:
        print("Database connection failed.")
        return

    create_tables()
    print("Employee table ready.")

    ui()


def main():
    print("Application initiated")
    application()


if __name__ == "__main__":
    main()