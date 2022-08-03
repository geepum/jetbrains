#!/opt/homebrew/opt/python@3.10/bin/python3

print('How many pencils would you like to use:')
while True:
    try:
        num_or_not = int(input())
    
    except (ValueError, TypeError):
        print('The number of pencils should be numeric')

    else:
        if num_or_not < 1:
            print('The number of pencils should be positive')
        else:
            break


print('Who will be the first (John, Jack):')
while True:
    who_first = input()

    if who_first == 'John' or who_first == 'Jack':
        break
    else:
        print("Choose between 'John' and 'Jack'")


pipe = '|'
num = int(num_or_not)
print(f'{pipe * num}')
print(f'''{who_first}'s turn!''')

# looping = True
while num > 0:
    try:
        left_over = int(input())

    except (TypeError, ValueError):
        print("Possible values: '1', '2' or '3'")

    else:
        if left_over > 3 or left_over < 1:
            print("Possible values: '1', '2' or '3'")
            
        elif left_over > num:
            print('Too many pencils were taken')
        else:
            num -= left_over
            if who_first == 'John':
                who_first = 'Jack'
            else:
                who_first = 'John'

            if num == 0:
                break
            else:
                print(f"{pipe * num}")
                print(f"{who_first}'s turn!")

print(f"{who_first} won!")