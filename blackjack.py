import random

x = 0

def draw():
	hand = random.randint(1,11)
	return hand

for _ in range(2):
	card = draw()
	x += card
	print 'Card: ' + str(card)

print 'Total: ' + str(x)

while x < 21:
	hit = raw_input('Hit? (Y/N): ')
	if hit == 'y':
		card = draw()
		x += card
		print 'Card: ' + str(card)
		print 'Total: ' + str(x)
	if hit == 'n':
		break
	else:
		print 'What is that?'
else:
	print 'You a busta'