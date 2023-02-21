def flash_card():
    
	num_of_cards = int(input('Input the number of cards:\n'))
	base1 = 1
	base2 = 0
	lst_term = []
	lst_definition = []

	while base1 <= num_of_cards:
		term = input(f'The term for card #{base1}:\n')
		lst_term.append(term)

		definition = input(f'The definition for card #{base1}:\n')
		lst_definition.append(definition)

		base1 += 1

	while base2 < len(lst_term):

		answer = input(f'Print the definition of "{lst_term[base2]}":\n')

		if answer == lst_definition[base2]:
			print('Correct!')
		else:
			print(f'Wrong. The right answer is "{lst_definition[base2]}".')

		base2 += 1


flash_card()