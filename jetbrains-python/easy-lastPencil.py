#!/opt/homebrew/opt/python@3.10/bin/python3

'''if pencils % 4 == 0, then 3
if pencils % 4 == 3 then  2
if pencils % 4 == 2 then  1'''



while True:
    try:
        how_many_pencils = int(input('How many pencils would you like to use:\n'))
    
    except (ValueError, TypeError):
        print('The number of pencils should be numeric')

    else:
        if how_many_pencils < 1:
            print('The number of pencils should be positive')
        else:
            break


while True:
    
    who_first = input('Who will be the first (John, Jack):\n')
    
    if who_first == 'John' or who_first == 'Jack':
        break
    else:
        print("Choose between 'John' and 'Jack'")


pipe = '|'
remainder = int(how_many_pencils)
player = 'John'
bot = 'Jack'
last_player = ''
print(f'{pipe * remainder}')

def player_move(num):
    while True:
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
                return left_over


def bot_move(num):
    if num % 4 == 0:
        return 3
    elif num % 4 == 3:
        return 2
    elif num % 4 == 2:
        return 1
    elif num % 4 == 1:
        return 1


while remainder > 0:

    if who_first == player:
        print("John's turn!")

        num1 = player_move(remainder)
        remainder -= num1

        if remainder != 0:
            num2 = bot_move(remainder)

            print(f'{pipe * remainder}')

            print("Jack's turn:")
            print(num2)
            remainder -= num2
            last_player = player
            print(f'{pipe * remainder}')
        else:
            last_player = bot
            break

    elif who_first == bot:
        print("Jack's turn!")

        num_one = bot_move(remainder)
        print(num_one)

        remainder -= num_one

        if remainder != 0:
            print(f'{pipe * remainder}')

            print("John's turn!")
            num_two = player_move(remainder)

            remainder -= num_two
            print(f'{pipe * remainder}')

            last_player = bot
        else:
            last_player = player
            break
    

print(f'{last_player} won!')