msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n" 
msg_5 = "Do you want to continue calculations? (y / n):\n"

memory = 0

def calc():
    x, oper, y = input(msg_0).split()
    return x, oper, y


while True:
    calc()

    if x == 'M':
        x = M
    elif y == 'M':
        y = M
    else:
        pass

    try:
        x = float(x)
        y = float(y)

    except (ValueError, TypeError):
        print(msg_1)

    else:
        if oper in ['+', '-', '*', '/']:
            if oper == '+':
                result = x + y

            elif oper == '-':
                result = x - y
            
            elif oper == '*':
                result = x * y

            elif oper == '/' and y != 0:
                result = x / y

            

            print(result)
            memory = result if input(msg_4) == 'y' else 0

            if input(msg_5) == 'y':
                M = memory
                continue
            else:
                break
            
        elif oper == '/' and y == 0:
            print(msg_3)

        else:
            print(msg_2)