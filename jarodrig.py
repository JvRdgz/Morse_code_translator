"""
CONVERSOR TEXTO A MORSE.
	Primero de todo, compruebo que el numero de argumentos introducidos 
	es correcto. Recojo el argumento 'argv[1]' y lo guardo en la variable text.
	Lo convierto a mayusculas. Creo un diccionario con las key como
	las letras del alfabeto y su correspondiente valor en morse.
	Creo una variable 'morse' en la cual, voy a guardar el resultado final
	del texto convertido a morse. Creo un for que va a recorrer el texto ingresado
	por teclado y despues otro for que va a recorrer el diccionario. A continuacion,
	compruebo si la letra actual del texto coincide con alguna del diccionario y,
	en ese caso, guardo en 'morse' el valor de esa coincidencia. Una vez hecho esto,
	termina de buscar con la letra del texto actual y pasa a la siguiente letra de
	dicho texto. Si en el texto encuentra un espacio, lo guardara en la variable 'morse'
	como '/', el cual indiquica el comienzo de otra palabra. Una vez terminado el primer
	bucle, imprime el resultado final.

	Es mi segundo programa que hago en python en toda mi vida. El primero fue un Hello World!.
	Me llevo una tarde completar el programa dado que he tenido que aprender varias cosas y
	conceptos propios de python.
"""

# PARA EL USO DE ARGUMENTOS EN LA EJECUCION DEL PROGRAMA
import sys
# EN EL CASO EN QUE QUIERA LEER POR TECLADO AL EJECUTAR EL PROGRAMA SIN PASAR ARGUMENTOS.
# print('Introduce texto:')
# text = input()

if (len(sys.argv) != 2):
	print('Error, es preciso ejecutar con almenos un argumento')
else:
	text = sys.argv[1]
	text = text.upper()
	# text = [text]
	# print(type(text))
	# print(text)
	CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
		'D': '-..', 'E': '.', 'F': '..-.',
		'G': '--.', 'H': '....', 'I': '..',
		'J': '.---', 'K': '-.-', 'L': '.-..',
		'M': '--', 'N': '-.', 'O': '---',
		'P': '.--.', 'Q': '--.-', 'R': '.-.',
		'S': '...', 'T': '-', 'U': '..-',
		'V': '...-', 'W': '.--', 'X': '-..-',
		'Y': '-.--', 'Z': '--..',
		}
	morse = ""

	for word in text:
		for key in CODE:
			if word == key:
				morse += CODE[key] + " "
				# print (word, ":", CODE[key])
				break;
		if word == " ":
			morse += " / "
	print(morse)
"""
def loop():
	for word in text:
		for key in CODE:
			if word == key:
				morse += CODE[key] + " "
				print (word, ":", CODE[key])
				break;
			if word == " ":
				morse += " / "
	print(morse)
"""
