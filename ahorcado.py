#incorporar comprehensions
#investigar funcion enumerate
#el metodo get de los diccionarios puede servir
#para limpiar la pantalla usar os.system("cls")

import random


def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word)
            #select the random word
            randomWord = random.choice(words)
            return randomWord


def normalize():
    # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s


def run ():
    read()

if __name__ ==  '__main__':
    run()
