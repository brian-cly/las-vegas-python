import random

total = 0

def draw():
	hand = random.randint(1,11)
	return hand

for _ in range(2):
	card = draw()
	total += card
	print 'Card: ' + str(card)

print 'Total: ' + str(total)

while total < 21:
	hit = raw_input('Hit? (Y/N): ')
	if hit == 'y':
		card = draw()
		total += card
		print 'Card: ' + str(card)
		print 'Total: ' + str(total)
	elif hit == 'n':
		break
	else:
		print 'What is that?'
else:
	print 'You a busta'