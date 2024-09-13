
def calculator(sum_):
    split_sum = sum_.split()
    sum__ = 0
    operators = ['+', '-', '//','/','*']

    for i in sum_:
        if i in operators:
            if i == '+':
                sum__ += int(split_sum[split_sum.index(i) + 1])
            elif i == '-':
                sum__ -= int(split_sum[split_sum.index(i) + 1])
            elif i == '//':
                sum__ = sum__ // int(split_sum[split_sum.index(i) + 1])
            elif i == '/':
                sum__ = sum__ / int(split_sum[split_sum.index(i) + 1])
            elif i == '*':
                sum__ *= int(split_sum[split_sum.index(i) + 1])
        
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
operator = input("what operator e.g[+,-,*,/]: ")



if __name__ == "__main__":
    # sum_ = str(input(""))
    # print(calculator(sum_))
    if operator == "+":
        print(add(a,b))

    elif operator == "-":
        print(subtract(a,b))

    elif operator == "*":
        print(multiply(a,b))

    elif operator == "/":
        print(divide(a,b))