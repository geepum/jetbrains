def flash_card():
	term = input()
	definition = input()
	answer = input()
    

	if definition == answer:
		print('Your answer is right!')
	else:
		print('Your answer is wrong...')


flash_card()