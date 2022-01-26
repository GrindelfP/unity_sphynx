def check_code(correct_code: str, current_code: list) -> bool:
    is_fitting: bool = True
    for i in range(len(correct_code)):
        if correct_code[i] != str(current_code[i]):
            is_fitting = False
            break

    return is_fitting


def code_pick(u_code) -> list:
    code: list = []
    for times in range(len(u_code)):
        code.append(0)
    for index in range(len(code)-1, -1, -1):
        code[index] += 1
        if check_code(u_code, code):
            return code

    # for i in range(0, 10):
    #     for j in range(0, 10):
    #         for k in range(0, 10):
    #             for m in range(0, 10):
    #                 picked_code: str = str(i) + str(j) + str(k) + str(m)
    #                 if check_code(u_code, picked_code):
    #                     return picked_code


print(code_pick("2345"))
