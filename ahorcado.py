import random
import os


def normalize(s):
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
    try:
        
        words = []
        with open("./archivos/data.txt", "r", encoding= "utf-8") as f:
            for word in f:
                words.append(word)
                randomWord = random.choice(words)
                currentWord = list("_" * len(randomWord))
                while(randomWord != currentWord):
                    print("Empieza el juego! \n\n")
                    #currentWord = list("_" * len(randomWord))
                    print(currentWord)
                    letter = normalize(input("\n\nIngrese una letra: "))
                    if letter in currentWord:
                        randomWord = list(randomWord)
                        for i,x in enumerate(randomWord):
                            if x == letter:
                                currentWord = "".join(currentWord)
                    os.system("cls")
                print(f'Ganaste! Tu palabra era {randomWord}')

    except ValueError: 
        print("Solo debes ingresar letras")
 
    

if __name__ ==  '__main__':
    run()
