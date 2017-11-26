import random
import sys

deck_hearts = ['Ace_hearts', 'King_hearts', 'Queen_hearts', 'Jack_hearts', 
	'10_hearts', '9_hearts', '8_hearts', '7_hearts', '6_hearts', 
	'5_hearts', '4_hearts', '3_hearts', '2_hearts']

deck_diamonds = ['Ace_diamonds', 'King_diamonds', 'Queen_diamonds', 'Jack_diamonds', 
	'10_diamonds', '9_diamonds', '8_diamonds', '7_diamonds', '6_diamonds', 
	'5_diamonds', '4_diamonds', '3_diamonds', '2_diamonds']

deck_spades = ['Ace_spades', 'King_spades', 'Queen_spades', 'Jack_spades', 
	'10_spades', '9_spades', '8_spades', '7_spades', '6_spades', 
	'5_spades', '4_spades', '3_spades', '2_spades']

deck_clubs = ['Ace_clubs', 'King_clubs', 'Queen_clubs', 'Jack_clubs', 
	'10_clubs', '9_clubs', '8_clubs', '7_clubs', '6_clubs', 
	'5_clubs', '4_clubs', '3_clubs', '2_clubs']


master_deck = {'Ace_hearts' : 14, 'King_hearts' : 13, 'Queen_hearts' : 12, 'Jack_hearts' : 11, 
'10_hearts' : 10, '9_hearts' : 9, '8_hearts' : 8, '7_hearts' : 7, '6_hearts' : 6, 
'5_hearts' : 5, '4_hearts' : 4, '3_hearts' : 3, '2_hearts' : 2, 'Ace_diamonds' : 14, 'King_diamonds' : 13, 'Queen_diamonds' : 12, 'Jack_diamonds' : 11, 
'10_diamonds' : 10, '9_diamonds' : 9, '8_diamonds' : 8, '7_diamonds' : 7, '6_diamonds' : 6, '5_diamonds' : 5, '4_diamonds' : 4, 
'3_diamonds' : 3, '2_diamonds' : 2, 'Ace_spades' : 14, 'King_spades' : 13, 'Queen_spades' : 12, 'Jack_spades' : 11, 
'10_spades' : 10, '9_spades' : 9, '8_spades' : 8, '7_spades' : 7, '6_spades' : 6, 
'5_spades' : 5, '4_spades' : 4, '3_spades' : 3, '2_spades' : 2, 'Ace_clubs' : 14, 'King_clubs' : 13, 'Queen_clubs' : 12, 'Jack_clubs' : 11, 
'10_clubs' : 10, '9_clubs' : 9, '8_clubs' : 8, '7_clubs' : 7, '6_clubs' : 6, 
'5_clubs' : 5, '4_clubs' : 4, '3_clubs' : 3, '2_clubs' : 2}

deck_red = deck_hearts + deck_diamonds
deck_black = deck_clubs + deck_spades
full_deck = deck_black + deck_red


def first_turn():
	print('Red or Black ? (R/B)')
	global first_card
	first_card = random.choice(full_deck)
	full_deck.remove(first_card)
	#print('DEBUG !! FIRST CARD = ' + str(first_card)) #DEBUG
	print('>>> ', end="")
	guess = input()
	print()
	while guess != 'R' and guess != 'r' and guess != 'Red' and guess != 'B' and guess != 'b' and guess !='Black': # Make sure user complies 
		print('Please enter only R or B')
		print('>>>', end="")
		guess = input()
	if guess == 'R' or guess == 'r' or guess == 'Red':
		if first_card in deck_red:
			print('First round won :)')
			print('First card = ' + str(first_card))
			print()
			second_turn()
		else:
			sys.exit('First round lost :(')
	elif guess == 'B' or guess == 'b' or guess == 'Black':
		if first_card in deck_black:
			print('First round won :)')
			print('First card = ' + str(first_card))
			print()
			second_turn()
		else:
			sys.exit('First round lost :(')

def second_turn():
	print('+ or - ? (+/-)')
	global second_card
	second_card = random.choice(full_deck)
	full_deck.remove(second_card)
	#print('DEBUG !! SECOND CARD = ' + str(second_card)) #DEBUG
	print('>>> ', end="")
	second_guess = input()
	while second_guess != '+' and second_guess != '-':
		print('Please enter only + or -')
		print('>>>', end="")
		second_guess = input()
	print()
	if second_guess == '+':
		if master_deck[first_card] < master_deck[second_card]:
			print('Second round won :)')
			print('Second card = ' + str(second_card))
			print()
			third_turn()
		else:
			sys.exit('Second round lost :(')
	elif second_guess == '-':
		if master_deck[first_card] < master_deck[second_card]:
			sys.exit('Second round lost :(')
		else:
			print('Second round won :)')
			print('Second card = ' + str(second_card))
			print()
			third_turn()

def third_turn():
	print('Inside ou Outside ? (I/O)')
	global third_card
	third_card = random.choice(full_deck)
	full_deck.remove(third_card)
	#print('DEBUG !! THIRD CARD = ' + str(third_card)) #DEBUG
	print('>>> ', end="")
	third_guess = input()
	while third_guess != 'I' and third_guess != 'i' and third_guess !='Inside' and third_guess != 'O' and third_guess != 'o' and third_guess != 'Outside':
		print('Please enter only I (for Inside) or O (for Outside)')
		print('>>>', end="")
		third_guess = input()
	print()
	if third_guess == 'I' or third_guess == 'i' or third_guess == 'Inside':
		if (master_deck[first_card]) <= (master_deck[third_card]) <= (master_deck[second_card]) or (master_deck[second_card]) <= (master_deck[third_card]) <= (master_deck[first_card]):
			print('Third round won :)')
			print('Third card = ' + str(third_card))
			print()
			fourth_turn()
		else:
			sys.exit('Third round lost :(')
	elif third_guess == 'O' or third_guess == 'o' or third_guess == 'Outside':
		if ((master_deck[third_card]) < (master_deck[first_card]) and (master_deck[third_card]) < (master_deck[second_card])) or ((master_deck[third_card]) > (master_deck[first_card]) and (master_deck[third_card]) > (master_deck[second_card])):
			print('Third round won :)')
			print('Third card = ' + str(third_card))
			print()
			fourth_turn()
		else:
			sys.exit('Third round lost :(')

def fourth_turn():
	print('Sign ? (H/D/S/C)')
	global fourth_card
	fourth_card = random.choice(full_deck)
	full_deck.remove(fourth_card)
	#print('DEBUG !! FOURTH CARD = ' + str(fourth_card)) #DEBUG
	print('>>>', end="")
	fourth_guess = input()
	while fourth_guess != 'H' and fourth_guess != 'h' and fourth_guess != 'Hearts' and fourth_guess != 'D' and fourth_guess != 'd' and fourth_guess != 'Diamonds' and fourth_guess != 'S' and fourth_guess != 's' and fourth_guess != 'Spades' and fourth_guess != 'C' and fourth_guess != 'c' and fourth_guess != 'Clubs':
		print('Please enter only H (Hearts), D (Diamonds), S (Spades), C (Clubs)')
		print('>>>', end="")
		fourth_guess = input()
	print()
	if fourth_guess == 'H' or fourth_guess == 'h' or four_guess == 'Hearts':
		if fourth_card in deck_hearts:
			sys.exit('Congrats, you won !!!')
		else:
			sys.exit('Last round lost :(')
	elif fourth_guess == 'D' or fourth_guess == 'd' or fourth_guess == 'diamonds':
		if fourth_card in deck_diamonds:
			sys.exit('Congrats, you won !!!')
		else:
			sys.exit('Last round lost :(')
	elif fourth_guess == 'S' or fourth_guess == 's' or fourth_guess == 'spades':
		if fourth_card in deck_spades:
			sys.exit('Congrats, you won !!!')
		else:
			sys.exit('Last round lost :(')
	elif fourth_guess == 'C' or fourth_guess == 'c' or fourth_guess == 'Clubs':
		if fourth_card in deck_clubs:
			sys.exit('Congrats, you won !!!')
		else:
			sys.exit('Last round lost :(')

while full_deck:
	first_turn()
