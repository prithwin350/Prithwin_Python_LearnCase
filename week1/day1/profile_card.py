def get_experience():
    while True:
        try:
            experience = int(input("Enter your experience: "))
            return experience
        except ValueError:
            print("Invalid input. Please enter your experience as a number.")


def profile_card():
    print('Welcome to the Profile Card Generator!')
    name = input('Enter your name:')
    role = input('Enter your role:')
    experience = get_experience()
    print('Hello, ' + name)
    print('You are a ' + role)
    print('You have ' + str(experience) + ' years of experience')

def main():
    profile_card()

main()