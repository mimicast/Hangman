import random

# List of words to use in the game.
wordList = ['computer', 'guitar', 'elephant', 'basketball', 'pineapple', 'strawberry', 'rainbow', 'mountain', 'butterfly', 'universe']
listLength = len(wordList)
foundLetters = [] # Keeps a track of the indexes found for the selected word.

# Prints the required ASCII art depending on the number of failures.
def hangmanAscii(failure):
    if failure == 1:
        print('''
                  _______
                 |/      |
                 |      (_)
                 |      
                 |      
                 |      
                 |
             ____|___''')
    elif failure == 2:
          print('''
                  _______
                 |/      |
                 |      (_)
                 |       |
                 |       
                 |      
                 |
             ____|___''')
    elif failure == 3:
          print('''
                  _______
                 |/      |
                 |      (_)
                 |       |
                 |       |
                 |      
                 |
             ____|___''')
    elif failure == 4:
          print('''
                  _______
                 |/      |
                 |      (_)
                 |      \|
                 |       |
                 |      
                 |
             ____|___''')
    elif failure == 5:
          print('''
                  _______
                 |/      |
                 |      (_)
                 |      \|/
                 |       |
                 |      
                 |
             ____|___''')
    elif failure == 6:
          print('''
                  _______
                 |/      |
                 |      (_)
                 |      \|/
                 |       |
                 |      /
                 |
             ____|___''')
    else:
          print('''
                  _______
                 |/      |
                 |      (_)
                 |      \|/
                 |       |
                 |      / \
                 |
             ____|___''')


asciiTitle = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
'''

print("Welcome to...")
print(asciiTitle)

# Chooses a word at random from the list.
selectedWord = wordList[random.randint(0, listLength -1)]

print('''
     _______
    |/      |
    |      
    |      
    |      
    |      
    |
____|___''')

print("The computer has selected a word")

count = 0
blanks = ""

# Prints the necessary amount of blank spaces according to the length of the word. Its indexes correspond 1 to 1 to the indexes
# of the selected word.
while count < len(selectedWord):
    blanks = blanks + "_"
    count += 1

print(blanks)

# Initial values.
winner = False 
tries = 0
corrGuesses = 0

print("Guess a letter. You can also guess the word, but you only get ONE TRY.")
print("I wish you luck...")

# Captures and compares the Users' guess as long as they have not found the answer or haven't ran out of tries.
while winner == False:
    selection = input("Guess: ")
    # Verifies if the User has ran out of tries.
    if tries < len(selectedWord):
        # Verifies if the user is jus trying to guess a letter or the whole word.
        if len(selection) == 1:
            # Gets the Index of the selected letter.
            indexOfLetter = selectedWord.find(selection)
            # If the user guesses wrong, it adds 1 to the tries counter and prints the corresponding ASCII art
            if indexOfLetter == -1:
                tries += 1
                hangmanAscii(tries)
            else:
                # Verifies if the found letter was one we previously found.
                for n in foundLetters:
                    # if the letter was previously found, find the next one, starting from the last position + 1 and up to
                    # the length of the string.
                    if n == indexOfLetter:
                        indexOfLetter = selectedWord.find(selection, indexOfLetter + 1)
                # If the letter was found several times before, indexOfLetter will return -1, so this prevents the reprint of
                # blanks and stops adding to the foundLetters list further down.
                if indexOfLetter == -1:
                    print(f"You found all instances of the letter {selection}. Try another letter.")
                else:
                    # Adds the Index of the found letter to a list, to keep track of the letters found and check in case of duplicates..
                    foundLetters.append(indexOfLetter) 
                    # Replaces the index of one of the blank spaces with the index of the found letter and leaves the rest of the spaces
                    # blank.
                    blanks = blanks[:indexOfLetter] + selectedWord[indexOfLetter] + blanks[indexOfLetter+1:]
                    
                    corrGuesses += 1
                    if corrGuesses == len(selectedWord):
                        winner = True 
                    print(blanks)
        elif selection == "":
            print("Did you just press enter without a word? \nAccidents can happen, so you can try again.")
        else:
            # If the user guesses the right word, it changes the winner value to True, and the While breaks by itself.
            if selection == selectedWord:
                winner = True
            # If the user guesses wrong, it prints the full ASCII art and breaks out of the While loop.
            else:                
                hangmanAscii(7)
                break
    else:
        # If the user has ran out of tries, it breaks out of the While loop with the winner variable set to False.
        break

# Prints the correct end game message according to the value of the winner variable.
if winner == True:
    print(f"Congratulations! The word was '{selectedWord}'!")
else:
    print(f"You guessed wrong. The word was '{selectedWord}'. Game Over.")
