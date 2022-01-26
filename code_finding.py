from utility import loading


def code_checking(u_code: str) -> str:
    code: int = 0
    while code != int(u_code):
        code += 1
        loading()
    return ("0" * (len(u_code) - len(str(code)))) + str(code)
