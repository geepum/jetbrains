#!/opt/homebrew/opt/python@3.10/bin/python3

water = 400
milk = 540
beans = 120
cups = 9
money = 550


# coffee machine says
# def coffee_machine():
#   global water, milk, beans, cups, money

#   print(f'''The coffee machine has:
# {water} ml of water
# {milk} ml of milk
# {beans} g of coffee beans
# {cups} disposable cups
# ${money} of money
# ''')


# function - buy
def buy():
  global water, milk, beans, cups, money

  user_want = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n''')

  if user_want == '1' and water >= 250 and beans >= 16 and money >= 4:
    water -= 250
    beans -= 16
    money += 4

  elif user_want == '2' and water >= 350 and milk >= 75 and beans >= 20 and money >= 7:
    water -= 350
    milk -= 75
    beans -= 20
    money += 7

  elif user_want == '3' and water >= 200 and milk >= 100 and beans >= 12 and money >= 6:
    water -= 200
    milk -= 100
    beans -= 12
    money += 6

  elif user_want == 'back':
    print('')
    return None

  else:
    print('Sorry, not enough water!\n')
    return None

  cups -= 1
  print('I have enough resources, making you a coffee!\n')


# function - fill
def fill():
  global water, milk, beans, cups, money

  add_water = int(input('Write how many ml of water you want to add:\n'))
  add_milk = int(input("Write how many ml of milk you want to add:\n"))
  add_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
  add_cups = int(input("Write how many cups of coffee you want to add:\n"))

  water += add_water
  milk += add_milk
  beans += add_beans
  cups += add_cups


# function - take
def take():
  global water, milk, beans, cups, money
  print(f'\nI gave you ${money}\n')
  money = 0


# function - remaining
def remaining():
  global water, milk, beans, cups, money

  print(f'''
The coffee machine has:
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
{cups} disposable cups
${money} of money
''')


# function - choose action according to user_input
def user_action():

  while True:

    user_input = input('Write action (buy, fill, take, remaining, exit):\n')

    if user_input == 'buy':
      buy()
    elif user_input == 'fill':
      fill()
    elif user_input == 'take':
      take()
    elif user_input == 'remaining':
      remaining()
    elif user_input == 'exit':
      break
  

user_action()
