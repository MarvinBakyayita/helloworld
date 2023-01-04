#here we are writing the same code as "hellowolrd.py" 
#but in this case we are printing the output on the same line

def hello(to = "world"):
    print("Hello,", to.strip())

hello()  #here I am calling the already defined output "world"

name = input("What's your name? ").title()
hello(name)
