from config.database import check_connection, engine, Base
from ui.menu import ui


def application():
    print("Welcome to DEIENAMI")

    if check_connection():
        print("Database connection successful.")
    else:
        print("Database connection failed.")
        return

    Base.metadata.create_all(engine)
    print("Database ready.")

    ui()


def main():
    print("Application initiated")
    application()


if __name__ == "__main__":
    main()