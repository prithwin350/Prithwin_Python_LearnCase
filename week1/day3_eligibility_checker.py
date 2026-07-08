users = ["admin", "john", "alice", "mike", "sarah"]
passwords = ["admin123", "john123", "alice123", "mike123", "sarah123"]

def loan_eligibility_checker():
    print("Welcome to the Loan Eligibility Checker!\n")

    name = input("Enter your name: ")

    if name == "exit":
        print("Exiting the Loan Eligibility Checker. Goodbye!")
        return

    age = int(input("Enter your age: "))
    monthly_salary = float(input("Enter your monthly salary: "))
    employment_years = int(input("Enter years of employment: "))
    credit_score = int(input("Enter your credit score: "))
    existing_loan = input("Do you have an existing loan? yes/no: ").lower()

    loan_score = 0

    if age >= 21:
        loan_score += 20
    else:
        print("You must be at least 21 years old to apply for a loan.")
        return

    if monthly_salary >= 30000:
        loan_score += 25
    else:
        loan_score -= 25

    if employment_years >= 2:
        loan_score += 20
    else:
        loan_score -= 20

    if credit_score >= 650:
        loan_score += 25
    else:
        loan_score -= 25

    if existing_loan == "no":
        loan_score += 10
    else:
        loan_score -= 10

    print(f"\nLoan Score: {loan_score}/100")

    if loan_score >= 70:
        print(f"Loan Approved! Congratulations, {name}.")
    else:
        print(f"Loan Rejected. Sorry, {name}. MiNimum score required for loan approval is 70.")
def login_eligibility_checker():
    while True:
        username = input("Enter your username: ")

        if username in users:
            password = input("Enter your password: ")

            index = users.index(username)

            if password == passwords[index]:
                print("Login successful!\n")
                return True
            else:
                print("Incorrect password. Please try again.\n")
                continue

        else:
            print("Invalid username. Please try again.\n")

def main():
    print("Welcome to the Eligibility Checker!\n")
    is_logged_in=login_eligibility_checker()

    if is_logged_in==True:
        loan_eligibility_checker()

main()