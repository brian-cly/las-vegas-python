import random

total = 0
dealer = 0

def draw():
	hand = random.randint(1,11)
	return hand

for _ in range(2):
	user_card = draw()
	dealer_card = draw()
	total += user_card
	dealer += dealer_card
	print 'Card: ' + str(user_card)

print 'Total: ' + str(total)

while total < 21:
	hit = raw_input('Hit? (Y/N): ')
	if hit == 'Y' or hit == 'y':
		user_card = draw()
		total += user_card
		print 'Card: ' + str(user_card)
		print 'Total: ' + str(total)
	elif hit == 'N' or hit == 'n':
		print 'Dealer Total: ' + str(dealer)
		while dealer < 15:
			dealer_card = draw()
			dealer += dealer_card
			print 'Dealer Card: ' + str(dealer_card)
			print 'Dealer Total: ' + str(dealer)
			if dealer > 21:
				print 'Dealer a busta. You win!'
		if total < dealer:
			print 'Dealer wins!'
		elif total == dealer:
			print 'Tie game!'
		else:
			print 'You win!'
		break
	else:
		print 'I do not recognize your response.'
else:
	print 'You a busta'