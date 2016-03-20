import random

total = 0
dealer = 0
cash = 100000
bet = 1
rounds = 0
yes = ['Y','y','Yes','yes']
no = ['N','n','No','no']

def draw():
	hand = random.randint(1,11)
	return hand

def balance(result,bet,cash):
	if result == 'win':
		print 'You win $' + str(int(bet)) + '. You now have $' + str(int(cash)) + '.'
	elif result == 'lose':
		print 'You lose $' + str(int(bet)) + '. You now have $' + str(int(cash)) + '.'
	elif result == 'tie':
		print 'Tie game!'
		print 'Nothing happens. You have $' + str(int(cash)) + '.'

print 'You currently have $' + str(int(cash)) + '.'
while cash > 0:
	print 'You are betting $' + str(int(bet)) + '.'
	total = 0
	dealer = 0
	for _ in range(2):
		user_card = draw()
		dealer_card = draw()
		total += user_card
		dealer += dealer_card
		print 'Card: ' + str(user_card)
	print 'Total: ' + str(total)
	while total < 21:
		if total < 17:
			user_card = draw()
			total += user_card
			print 'Card: ' + str(user_card)
			print 'Total: ' + str(total)
		else:
			print 'Dealer Total: ' + str(dealer)
			while dealer < 17:
				dealer_card = draw()
				dealer += dealer_card
				print 'Dealer Card: ' + str(dealer_card)
				print 'Dealer Total: ' + str(dealer)
			if dealer > 21:
				print 'Dealer a busta. You win!'
				cash += bet
				balance('win',bet,cash)
			elif total < dealer:
				print 'Dealer wins!'
				cash -= bet
				balance('lose',bet,cash)
			elif total == dealer:
				balance('tie',bet,cash)
			else:
				print 'You win!'
				cash += bet
				balance('win',bet,cash)
			bet = bet * 2
			rounds += 1
			break
	else:
		if total == 21:
			print 'Blackjack! You win!'
			cash += 1.5*bet
			balance('win',1.5*bet,cash)
		else:
			print 'You a busta'
			cash -= bet
			balance('lose',bet,cash)
		bet = bet * 2
		rounds += 1
else:
	print 'Game Over. You lasted ' + str(rounds) + ' rounds.'