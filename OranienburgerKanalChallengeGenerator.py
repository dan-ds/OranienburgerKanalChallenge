import random

forbiddenList = {'B':33, 'D':55}

inputDeck = 'A' #Input deck defaults to A
allDecksList = ['A','B','C','D','E','F','Z']
allCardsList = list(range(1,61))
# NOTE: don't use [x]*y with nested lists.
allCardsListDrawn = {	'A':[False] * 60,
						'B':[False] * 60,
						'C':[False] * 60,
						'D':[False] * 60,
						'E':[False] * 60,
						'F':[False] * 60,}
allCardsFromDeckDrawn = {	'A':False,
							'B':False,
							'C':False,
							'D':False,
							'E':False,
							'F':False,}
# NOTE: Does not detect if fully drawn from one specific segment e.g., 21 to 40 (in the board game, all orange cards)
# So the code that checks from a completely exhausted deck is useless, but this situation never arises in a regular game of O.K. with official rules.

def drawCard(mydeck, mymin, mymax):
	while (True):
		if allCardsFromDeckDrawn[mydeck] == True:
			print('Error: Trying to draw from a completely exhausted deck.')
		draw = random.choice(allCardsList)
		# If between numbers (inclusive)
		if draw >= mymin and draw <= mymax:
			# If not drawn yet
			if not allCardsListDrawn[mydeck][draw-1]:
				# If not in forbidden list
				if not (mydeck in forbiddenList and forbiddenList[mydeck] == draw):
					# Set card to drawn, return card number
					allCardsListDrawn[mydeck][draw-1] = True
					# Tag whole deck as drawn if all cards of it are drawn:
					if all(i for i in allCardsListDrawn[mydeck]):
						print('Tagging deck '+mydeck+' as fully drawn.')
						allCardsFromDeckDrawn[mydeck] = True
					return draw

def chooseNextDeck(mydeck):
	newDeck = ''
	# If deck is not Z, return same deck
	if mydeck != 'Z':
		return mydeck
	# If deck is Z, then return a non-Z deck
	else:
		while newDeck == '' or newDeck == 'Z':
			newDeck = random.choice(allDecksList)
		return newDeck

print ("Oranienburger Kanal - Challenge Generator")
while (True):
	inputDeck = input('Type the letter of the deck you want to use (A, B, C, D, E, F) in CAPS\nor Z if you want to mix all decks\nand then press enter: ')
	if inputDeck in allDecksList:
		break

#Cards to draw:
#6 from 1 to 20
#5 from 21 to 40
#7 from 41 to 60

setupCards = ''
R1Cards = ''
R2Cards = ''
R3Cards = ''
R4Cards = ''
R5Cards = ''
R6Cards = ''
cardsDrawn = []

def oneCard(mymin, mymax):
	nextDeck = chooseNextDeck(inputDeck)
	return nextDeck + str(drawCard(nextDeck, mymin, mymax))

setupCards += oneCard(1,20)
setupCards += ', '
setupCards += oneCard(1,20)
setupCards += ', '
setupCards += oneCard(1,20)
setupCards += ', '
setupCards += oneCard(1,20)

R1Cards += oneCard(1,20)
R1Cards += ', '
R1Cards += oneCard(1,20)
R1Cards += ', '
R1Cards += oneCard(21,40)

R2Cards += oneCard(21,40)
R2Cards += ', '
R2Cards += oneCard(21,40)

R3Cards += oneCard(21,40)
R3Cards += ', '
R3Cards += oneCard(21,40)
R3Cards += ', '
R3Cards += oneCard(41,60)

R4Cards += oneCard(41,60)
R4Cards += ', '
R4Cards += oneCard(41,60)

R5Cards += oneCard(41,60)
R5Cards += ', '
R5Cards += oneCard(41,60)

R6Cards += oneCard(41,60)
R6Cards += ', '
R6Cards += oneCard(41,60)

print ('Setup the following cards: '+setupCards)
input('Press enter when you are at the end of Round 1')
print ('Add the following cards: '+R1Cards)
input('Press enter when you are at the end of Round 2')
print ('Add the following cards: '+R2Cards)
input('Press enter when you are at the end of Round 3')
print ('Add the following cards: '+R3Cards)
input('Press enter when you are at the end of Round 4')
print ('Add the following cards: '+R4Cards)
input('Press enter when you are at the end of Round 5')
print ('Add the following cards: '+R5Cards)
input('Press enter when you are at the end of Round 6')
print ('Add the following cards: '+R6Cards)
print('----------------------------------------------------------------------')
print('This is the text to copy to BGG:')
print('----------------------------------------------------------------------')
wallOfText = ''
wallOfText += 'This is a monthly challenge for Oranienburger Kanal.\n\nRules:\n'
wallOfText += '-For setup, use all the cards of the deck to block the top of the 2nd, 3rd and 4th action spaces: green, orange and blue, respectively.\n'
wallOfText += '-End of rounds 1, 3 and 6: When instructed to unblock the action space, remove the green, orange and blue cards from the top of the action spaces, respectively.\n'
wallOfText += '-Use advanced side of the board (if you don\'t know what to place, you can always place it exactly like the basic side).\n'
wallOfText += '-First, search setup cards (these are already ordered). Then, for each end of round search the next set of cards and order the river of cards accordingly.\n'
wallOfText += '-Post score for first blind playthrough.\n\n'
wallOfText += 'This month uses deck '+inputDeck+'.\n\n'
wallOfText += 'Setup cards: [o]'+setupCards+'[/o]\n\n'
wallOfText += 'End of Round 1: [o]'+R1Cards+'[/o] Also unblock top of 2nd action space. Order cards in the river.\n\n'
wallOfText += 'End of Round 2: [o]'+R2Cards+'[/o] Order cards in the river.\n\n'
wallOfText += 'End of Round 3: [o]'+R3Cards+'[/o] Also unblock top of 3rd action space. Order cards in the river.\n\n'
wallOfText += 'End of Round 4: [o]'+R4Cards+'[/o] Order cards in the river.\n\n'
wallOfText += 'End of Round 5: [o]'+R5Cards+'[/o] Order cards in the river.\n\n'
wallOfText += 'End of Round 6: [o]'+R6Cards+'[/o] Also unblock top of 4th action space. Order cards in the river.'
print(wallOfText)