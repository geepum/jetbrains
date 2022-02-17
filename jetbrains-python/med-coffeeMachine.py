#!/opt/homebrew/bin/python3

available_water = int(input('Write how many ml of water the coffee machine has:\n'))
available_milk = int(input('Write how many ml of milk the coffee machine has:\n'))
available_beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))

wanted_coffee = int(input('Write how many cups of coffee you will need:\n'))

need_water = 200
need_milk = 50
need_beans = 15


# check water
def check_water(a_water, n_water):
  return a_water // n_water


# check milk
def check_milk(a_milk, n_milk):
  return a_milk // n_milk


# check beans
def check_beans(a_beans, n_beans):
  return a_beans // n_beans


# check minimum
def minimum_availability():
  water = check_water(available_water, need_water)
  milk = check_milk(available_milk, need_milk)
  beans = check_beans(available_beans, need_beans)

  return min(water, milk, beans)


# compare with wanted
def compare_and_answer(demand):

  availability = minimum_availability()

  # if same amount
  if availability == demand:
    print(f'Yes, I can make that amount of coffee')

  # if more availble
  elif availability > demand:
    more = availability - demand
    print(f'Yes, I can make that amount of coffee and even {more} more than that')

  # if not availble
  else:
    print(f'No, I can make only {availability} cups of coffee')


compare_and_answer(wanted_coffee)