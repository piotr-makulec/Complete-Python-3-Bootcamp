from os import system

def update_display(display):
	system("clear || cls")
	print(" {} | {} | {} ".format(display[6], display[7], display[8]))
	print("--------------")
	print(" {} | {} | {} ".format(display[3], display[4], display[5]))
	print("--------------")
	print(" {} | {} | {} ".format(display[0], display[1], display[2]))

def check_score(display):
	for n in range(0, 3):
		if not display[n] == " ":
			if display[n] == display[n + 3] == display[n + 6]:
				return True
		if not display[n * 3] == " ":
			if display[n * 3] == display[n * 3 + 1] == display[n * 3 + 2]:
				return True
	if not display[4] == " ":
		if display[0] == display[4] == display[8] or display[2] == display[4] == display[6]:
			return True
	return False


print("KÓŁKO I KRZYŻYK")

current_display = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1 = 'R'
current_player = 1
new_move = "Jacek"
isinrange = False


while not player1 in ['O', 'X']:
	player1 = input("Gracz 1: kółko 'O' czy krzyżyk 'X'?\n")
	if not player1 in ['O', 'X']:
		print("Nie rozumiem, wpisz jeszcze raz")

if player1 == 'O':
	player2 = 'X'
else:
	player2 = 'O'

print("Wspaniale, w takim razie zaczynamy!")

update_display(["1", "2", "3", "4", "5", "6", "7", "8", "9"])



while True:
	print("Gracz {}, twoja kolej!".format(current_player))
	while not new_move.isdigit() or not isinrange: 
		new_move = input("Które pole wybierasz? (1 - 9)\n".format(current_player))
		if not new_move.isdigit():
			print("Nie rozumiem, wpisz jeszcze raz")
		elif int(new_move) in range(1, 10):
			if not current_display[int(new_move) - 1] == " ":
				print("Pole jest już zajęte! Wybierz inne.")
			else:
				isinrange = True
		else:
			print("Nie rozumiem, wpisz jeszcze raz")

	if current_player == 1:
		current_display[int(new_move) - 1] = player1
	else:
		current_display[int(new_move) - 1] = player2

	isinrange = False

	update_display(current_display)

	if check_score(current_display):
		print("Grę wygrał gracz {}. Gratulacje!".format(current_player))
		break

	if not " " in current_display:
		print("Remis!")
		break

	if current_player == 1:
		current_player = 2
	else:
		current_player = 1

