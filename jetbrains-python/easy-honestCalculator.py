msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


while True:

    x, oper, y = input(msg_0).split()

    try:
        x = float(x)
        y = float(y)

    except (ValueError, TypeError):
        print(msg_1)

    else:
        if oper == '+':
            result = x + y
            break

        elif oper == '-':
            result = x - y
            break
        
        elif oper == '*':
            result = x * y
            break

        elif oper == '/' and y != 0:
            result = x / y
            break
        
        else:
            print(msg_2)

