#adding function
def add(a,b):
    return a + b

#subtracting function
def subtract(a,b):
    return a - b

#dividing function
def divide(a,b):
    return a/b

#multkiplication function
def multiply(a,b):
    return a*b


if __name__ == "__main__":

    operator = None    
    
    #loop will run as long as the user does not type exit
    while operator != 'exit':

        operator = input("what operator e.g[+,-,*,/]: ")

        if operator == "exit":
            break

        else:

            a = int(input("enter your first number: "))
            b = int(input("enter your second number: "))

            if operator == "+":
                print('result: ',add(a,b))

            elif operator == "-":
                print('result: ',subtract(a,b))

            elif operator == "*":
                print('result: ',multiply(a,b))

            elif operator == "/":
                print('result: ',divide(a,b))

            else:
                print("invalid operator")