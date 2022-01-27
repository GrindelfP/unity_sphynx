from time import time
from code_finding import code_checking
from utility import receive_code, greetings

greetings()
users_code: str = receive_code()
current_time: float = time()
correct_code: str = code_checking(users_code)
total_time: float = time() - current_time
print("We are in! Your code was ", correct_code, "! \nWe've done the process in ", round(total_time, 8),
      " seconds.", sep="")
