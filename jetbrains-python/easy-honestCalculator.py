msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

while True:

    x, oper, y = input(msg_0).split()

    try:
        x = float(x)
        y = float(y)

    except (ValueError, TypeError):
        print(msg_1)

    else:
        if oper in ['+', '-', '*', '/']:
            if oper == '+':
                result = x + y
                print(result)
                break

            elif oper == '-':
                result = x - y
                print(result)
                break
            
            elif oper == '*':
                result = x * y
                print(result)
                break

            elif oper == '/' and y != 0:
                result = x / y
                print(result)
                break

            else:
                print(msg_3)
            
        else:
            print(msg_2)

