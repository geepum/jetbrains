msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n" 
msg_5 = "Do you want to continue calculations? (y / n):\n"

memory = 0


while True:
    x, oper, y = input(msg_0).split()

    if x == 'M':
        x = memory

    elif y == 'M':
        y = memory
    
    else:
        pass

    try:
        x = float(x)
        y = float(y)
        
    except (TypeError, ValueError):
        print(msg_1)
    
    else:
        if oper not in ['+', '-', '*', '/']:
            print(msg_2)
        elif oper == '/' and y == 0:
            print(msg_3)
        else:
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '*':
                result = x * y
            elif oper == '/' and y != 0:
                result = x / y

            print(result)

            if input(msg_4) == 'y':
                memory = result
            

            if input(msg_5) == 'n':
                break
            else:
                pass
            