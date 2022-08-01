#!/opt/homebrew/opt/python@3.10/bin/python3


memory = 0
math_ops = '+-*/'
msg_0 = 'Enter an equation'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = ''
msg_3 = 'Yeah... division by zero. Smart move...'


def calc():
    x, oper, y = input().split()

    try:
        x = float(x)
        y = float(y)

        x / y

    except (ValueError, TypeError):
        print(msg_1)

    except ZeroDivisionError:
        print(msg_3)

    else:
        if oper not in math_ops:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        
        else:
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '/':
                result = x / y
            elif oper == '*':
                result = x * y
    
    return result


print(eval('9 % 2'))