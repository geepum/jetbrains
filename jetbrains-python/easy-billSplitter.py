#!/usr/bin/python3

import random

num_of_friends = input(
    "Enter the number of friends joining (including you):\n")


def num_names_to_dict(num):
    dict_friends = {}

    for _ in range(num):
        name = input()
        dict_friends[name] = 0

    return dict_friends


def random_name(question, num, dictionary):
    if question == "Yes":
        lucky_num = random.randint(1, num-1)
        # print(lucky_num)
        lucky_person_value = list(dictionary)
        lucky_person = lucky_person_value[lucky_num]
        # print(lucky_person)
        print(f"\n{lucky_person} is the lucky one!\n")
        return lucky_person
    else:
        print("\nNo one is going to be lucky\n")


def billing_num(bill, question, num):
    if question == "Yes":
        bill = int(bill) / (num - 1)
    else:
        bill = int(bill) / num

    return bill


def splits(billing):
    if billing.is_integer():
        billing = int(billing)
    else:
        billing = round(billing, 2)

    return billing


def allocation(question, dictionary, lucky, splits):

    if question == "Yes":
        for person in list(dictionary):
            if person == lucky:
                dictionary[person] = 0
            else:
                dictionary[person] = splits
    else:
        for person in list(dictionary):
            dictionary[person] = splits

    print(dictionary)


try:
    num_friends = int(num_of_friends)
    if num_friends > 0:
        print("\nEnter the name of every friend (including you), each on a new line:")

        dict_friends = num_names_to_dict(num_friends)

        bill = input("\nEnter the total bill value:\n")

        lucky_q = input(
            '\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')

        lucky_person = random_name(lucky_q, num_friends, dict_friends)

        billing = billing_num(bill, lucky_q, num_friends)

        splits = splits(billing)

        allocation(lucky_q, dict_friends, lucky_person, splits)

    else:
        print("\nNo one is joining for the party")

except ValueError:
    print("No one is joining for the party")
