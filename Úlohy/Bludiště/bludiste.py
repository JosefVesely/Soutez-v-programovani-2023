# Josef Veselý

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()


def get_filepath():
    return filedialog.askopenfilename(title="Vyberte soubor s bludištěm", filetypes=(("Text file","*.txt"), ("all files","*.*")))

def print_maze(filepath):
    with open(filepath) as file:
        print(file.read())

def find_words(filepath):
    words = []

    with open(filepath) as file:
        maze = file.readlines()[1:] # První řádek je komentář

        for line in maze:
            line = line.strip()
            word = ""

            for char in line:
                if char == "#":
                    break
                elif char == " ":
                    # Prevrat slovo
                    try:
                        if word[-1].isupper():
                            word = word[::-1]
                    except IndexError:
                        continue

                    words.append(word)
                    word = ""
                else:
                    word += char   

    return words


filepath = get_filepath()
print_maze(filepath)
words = find_words(filepath)

if words:
    print(f"Nalezená slova: {', '.join(words)}")
else:
    print("Žádná nalezená slova")


input("Stiskněte Enter pro ukončení programu")