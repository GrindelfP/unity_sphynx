from code_finding import code_checking
from utility import receive_code, greetings

greetings()
users_code: str = receive_code()
print("We are in! Your code was ", code_checking(users_code), "!", sep="")
