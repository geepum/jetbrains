#!/opt/homebrew/opt/python@3.10/bin/python3

memory = 0
math_ops = '+-*/'
msg_0 = 'Enter an equation\n'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = 'Yeah... division by zero. Smart move...'
msg_4 = "Do you want to store the result? (y / n):\n" 
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"


def is_one_digit(v):
    if v > -10 and v < 10 and float.is_integer(v) == True:
        output = True
    else:
        output = False

    return output


def check(v1, v2, v3):
    msg = ''

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
            msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
                msg = msg + msg_8
    if (msg != ""):
        msg = msg_9 + msg

    print(msg)


def calc():
    x, oper, y = input(msg_0).split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    
    try:
        x = float(x)
        y = float(y)
    except (ValueError, TypeError):
        print(msg_1)
        
    else:
        if oper in '+-*/':

            check(x, y, oper)

            if oper == '+':
                result = x + y
                return result

            elif oper == '-':
                result = x - y
                return result

            elif oper == '*':
                result = x * y
                return result

            else:
                if oper == '/' and y != 0:
                    result = x / y
                    return result
                else:
                    print(msg_3)
        else:
            print(msg_2)


looping = True
while looping:
    calculation = calc()
    print(calculation)

    while looping:
        store = input(msg_4)

        if store == 'y':
            one_digit = is_one_digit(calculation)

            if one_digit:
                msg10 = input(msg_10)
                
                if msg10 == 'y':
                    msg11 = input(msg_11)

                    if msg11 == 'y':
                        msg12 = input(msg_12)

                        if msg12 == 'y':
                            memory = calculation

                        break
                    break
                break
            memory = calculation
            break
            
        else:
            memory = calculation
            break
        
    
    continum = input(msg_5)

    if continum == 'y':
        continue
    elif continum == 'n':
        looping = False
    else:
        break