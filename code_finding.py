def code_checking(u_code: str) -> str:
    code: int = 0
    produced_code: str = ""
    while code != int(u_code):
        code += 1
        produced_code = "0" * (len(u_code) - len(str(code))) + str(code)
        print("Let me think...", produced_code, end="\r")
    return produced_code
