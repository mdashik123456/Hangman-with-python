from dis import dis
import random

logo = ['''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/            ''']

#Stages of hangman

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#Rules of game and logo
print(logo[0])
print("-----------------------------------------------")
print("\nGuess the word/phrase before your man gets hung!")
# opening the file in read mode
my_file = open("WordList.txt", "r")
# reading the file , replacing end splitting the text and when newline ('\n') is seen with split().
word_list = my_file.read().split("\n")
my_file.close()

again = 'y'
while again == 'y':
    stages_Check = 6
    random_word = random.choice(word_list)

    # here display will create with blanck "_"
    display = []
    for i in random_word:
        display += "_"

    print(stages[stages_Check])
    while stages_Check > 0:
        check = 0
        print(" ".join(display))
        
        guess = input("Guess a char : ")
        for i in range(len(random_word)):
            random_word_char = random_word[i]
            #Check if guessing word is right or not
            if guess == random_word_char:
                display[i] = guess
                check = 1
        #If The Guessing char is wrong
        if check == 0:
            print("X== Wrong Guess ==X")
            #stages_Check decrement for lose a life
            stages_Check -= 1
        #Check Win or Lose
        if "_" not in display:
            print("".join(display))
            print("*** Congratulation ***\n***    You Win    ***")
            break
        print(stages[stages_Check])
    # If lose the show the messeges
    if "_" in display:
        print("X=== Sorry! You Lose ===X")
        print (f"The Word Was {random_word}")
    # Want to play again or not
    again = input("\n\nDo you want to play it again? (Y/N) : ")
    again = again.lower()
print ("\nThanks for playing this Game\n")