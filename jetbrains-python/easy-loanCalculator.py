#!/opt/homebrew/bin/python3
import math

# user input - loan principal
loan_principal = int(input('Enter the loan principal:\n'))
calc_method = input(f'''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n''')


# calculator
def calculator(calc_method):

  # function - monthly payment
  if calc_method == "m":
    monthly_payment(loan_principal)

  # function - number of months
  else:
    number_of_months(loan_principal)


# function - answer to monthly payment
def monthly_payment(loan):
  payment = int(input('Enter the monthly payment:\n'))
  months = math.ceil(loan / payment)

  if months == 1:
    print(f'It will take 1 month to repay the loan')
  else:
    print(f'It will take {months} months to repay the loan')


# functioin - answer to number of months
def number_of_months(loan):
  month_number = int(input('Enter the number of months:\n'))
  installments = math.ceil(loan / month_number)
  last_pay = loan - (installments * (month_number - 1))

  if loan % month_number == 0:
    print(f'Your monthly payment = {installments}')
  else:
    print(f'Your monthly payment = {installments} and the last payment = {last_pay}')



calculator(calc_method)
