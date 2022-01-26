def receive_code() -> str:
    while True:
        u_code = input("Enter the code. It must contain only of digits: ")
        try:
            int(u_code)
            return u_code
        except ValueError:
            print("You must use only integers!")
