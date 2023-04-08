import os, sys, time


#Tablero que siempre se muestra y actualiza
def Tablero():
	print('Jugador 1: ', wins1, '   Jugador 2: ', wins2, '   S para salir')
	print()
	print('Lugares:')
	print('1 2 3\n4 5 6\n7 8 9')
	print()
	print()
	print(espacios['1'] + '|' + espacios['2'] + '|' + espacios['3'])
	print('-+-+-')
	print(espacios['4'] + '|' + espacios['5'] + '|' + espacios['6'])
	print('-+-+-')
	print(espacios['7'] + '|' + espacios['8'] + '|' + espacios['9'])
	#Al mostrar tablero va a checar si sigue el juego
	Chequeo()


#Para el turno del jugador 1 (X)
def Turno1():
	print()
	print()
	while True:
		jugador1 = input('Turno jugador 1: ')
		#Asegurarnos que exista el espacio dado
		if jugador1 in espacios:
			#Si esta ocupado el lugar se pide nuevamente
			if espacios[jugador1] != ' ':
				print('Espacio ocupado. Intente de nuevo.')
			#Si esta vacío se guarda
			else:
				espacios[jugador1] = 'X'
				break
		else:
			#Para salir del juego se presiona S
			if jugador1 == 'S':
				sys.exit()
			#Casilla que no exista
			else:
				print('Posición no existe. Intente de nuevo.')


#Para el turno del jugador 2 (O)
def Turno2():
	print()
	print()
	while True:
		jugador2 = input('Turno jugador 2: ')
		#Asegurarnos que exista el espacio dado
		if jugador2 in espacios:
			#Si esta ocupado el lugar se pide nuevamente
			if espacios[jugador2] != ' ':
				print('Espacio ocupado. Intente de nuevo.')
			#Si esta vacío se guarda
			else:
				espacios[jugador2] = 'O'
				break
		else:
			#Para salir del juego se presiona S
			if jugador2 == 'S':
				sys.exit()
			#Casilla que no exista
			else:
				print('Posición no existe. Intente de nuevo.')


#Checar en todo momento si hay ganador o se acabo
#Se gane o se acabe se muestra el mensaje, se acaba, se borra y se reinicia
def Chequeo():
	global wins1
	global wins2
	global gameOver
	if ' ' not in espacios.values():
		print('Game Over')
		time.sleep(5)
		gameOver = True
		os.system('clear')
		Reinicio()
	#Todas las posibilidades de victoria
	if espacios['1'] == 'X' and espacios['2'] == 'X' and espacios[
	    '3'] == 'X' or espacios['4'] == 'X' and espacios['5'] == 'X' and espacios[
	        '6'] == 'X' or espacios['7'] == 'X' and espacios[
	            '8'] == 'X' and espacios['9'] == 'X' or espacios[
	                '1'] == 'X' and espacios['4'] == 'X' and espacios[
	                    '7'] == 'X' or espacios['2'] == 'X' and espacios[
	                        '5'] == 'X' and espacios['8'] == 'X' or espacios[
	                            '3'] == 'X' and espacios['6'] == 'X' and espacios[
	                                '9'] == 'X' or espacios[
	                                    '1'] == 'X' and espacios[
	                                        '5'] == 'X' and espacios[
	                                            '9'] == 'X' or espacios[
	                                                '3'] == 'X' and espacios[
	                                                    '5'] == 'X' and espacios[
	                                                        '7'] == 'X':
		print('1 WINS')
		wins1 = wins1 + 1
		time.sleep(5)
		gameOver = True
		os.system('clear')
		Reinicio()
	#Todas las posibilidades de victoria
	if espacios['1'] == 'O' and espacios['2'] == 'O' and espacios[
	    '3'] == 'O' or espacios['4'] == 'O' and espacios['5'] == 'O' and espacios[
	        '6'] == 'O' or espacios['7'] == 'O' and espacios[
	            '8'] == 'O' and espacios['9'] == 'O' or espacios[
	                '1'] == 'O' and espacios['4'] == 'O' and espacios[
	                    '7'] == 'O' or espacios['2'] == 'O' and espacios[
	                        '5'] == 'O' and espacios['8'] == 'O' or espacios[
	                            '3'] == 'O' and espacios['6'] == 'O' and espacios[
	                                '9'] == 'O' or espacios[
	                                    '1'] == 'O' and espacios[
	                                        '5'] == 'O' and espacios[
	                                            '9'] == 'O' or espacios[
	                                                '3'] == 'O' and espacios[
	                                                    '5'] == 'O' and espacios[
	                                                        '7'] == 'O':
		print('2 WINS')
		wins2 = wins2 + 1
		time.sleep(5)
		gameOver = True
		os.system('clear')
		Reinicio()


#Reiniciar juego
def Reinicio():
	global espacios
	espacios = {
	    '1': ' ',
	    '2': ' ',
	    '3': ' ',
	    '4': ' ',
	    '5': ' ',
	    '6': ' ',
	    '7': ' ',
	    '8': ' ',
	    '9': ' '
	}
	#Llamar tablero para mostrar el reinicio
	Tablero()


conteo = 0
wins1 = 0
wins2 = 0
espacios = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
}

while True:
	gameOver = False
	while gameOver == False:
		if gameOver == False:
			os.system('clear')
		if gameOver == False:
			Tablero()
		if gameOver == False:
			Turno1()
		if gameOver == False:
			os.system('clear')
		if gameOver == False:
			Tablero()
		if gameOver == False:
			Turno2()
		if gameOver == False:
			os.system('clear')
		if gameOver == False:
			Tablero()
		if gameOver == False:
			os.system('clear')