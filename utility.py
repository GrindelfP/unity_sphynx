def greetings() -> None:
    print("\t\tWelcome to the Advanced Aegyptian Tactics!"
          "\n\n\tThis AAT's product is called Unity Sphynx. "
          "\n\tIt receives your code and decodes the secret door, which is locked "
          "\nwith your code. The code must contain only of digits without spaces and "
          "\nbe up to 8 digits."
          "\n\tWarning! If You want to lock the door with more than 6-digit code "
          "\nit would take long to find the correct code, so prepare to be patient!")


def receive_code() -> str:
    while True:
        u_code = input("\nEnter the code -> ")
        if len(u_code) > 8:
            print("Your code should be no longer than 8 digits!")
        else:
            try:
                int(u_code)
                return u_code
            except ValueError:
                print("You must use only integers without spaces!")


def is_exit_possible() -> bool:
    while True:
        exit_possibility = input("Do you want to continue? (Y/N) ")
        if exit_possibility.upper() == "N":
            return False
        elif exit_possibility.upper() == "Y":
            return True
        elif exit_possibility.upper() != "Y":
            print("I don't quite understand you!")

