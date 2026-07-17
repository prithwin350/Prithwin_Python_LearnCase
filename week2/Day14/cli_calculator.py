import argparse

def add(num1,num2):
    process=num1+num2
    return process

def subtract(num1,num2):
    process=num1-num2
    return process

def multiply(num1,num2):
    process=num1*num2
    return process

def divide(num1,num2):
    process=num1/num2
    return process

def main():
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    parser = argparse.ArgumentParser(
        description="A simple command-line calculator."
    )

    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform"
    )

    parser.add_argument(
        "num1",
        type=int,
        help="First number"
    )

    parser.add_argument(
        "num2",
        type=int,
        help="Second number"
    )

    args = parser.parse_args()

    try:
        result = operations[args.operation](args.num1, args.num2)
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")


if __name__ == "__main__":
    main()