# Message to people reading the code:
# Please do not get overwhelmed if you find that there is a lot to go through. If your Computer Science teacher made you create a
# project, or you do this as part of a hobby, then simply read through the code, read the line-by-line explanation in the comments, and
# try to understand it as best as you can.

# -------------------
# IMPORTS - Prebuilt code that we need to perform certain functions
# -------------------
import random # Needed to select random word.


# -------------------
# VARIABLES - Containerps that store information in memory that we will use later
# -------------------
words = [] # `words` is defined as an empty array, which will later have a lot of different words from where will we randomly choose one for the game.

# This section of code reads the file `wordlist.txt`, which is a text file which has 58,000 words to choose from, and saves them all to `words`.
# Please read the disclaimer at the bottom of the text about this file.
with open("wordlist.txt", "r") as file: # `wordlist.txt` file is opened containing all our words, and is given the name `file`.
    # The benefit of using `with open() as file:` is that the file closes automatically, even if an error occurs,
    # meaning that there is no file left open in memory, and our code is kept cleaner and more understandable.
    words = file.read().split("\n") # Each word is stored is seperated by a line, and we seperate them using the newline character – `\n` - which is at the end of every line.

# The number of attmpts the player has.
attempts = 5

# Tells our program wether or not the player has won.
won = False

# Stores all the correctly guessed letters.
lettersGuessed = []

# Stores all the incorrectly guessed letters.
lettersIncorrectlyGuessed = []

# Selects a random word from the word list we made earlier.
word = random.choice(words)


# -------------------
# FUNCTIONS - Short blocks of code that can be called and ran by a name instead of being repeated. It also makes code more readible, as you can 
#             tell what the code does from the name of the function.
# -------------------
# This function checks the word to see if we have guessed all the letters
def checkWord(letters, word): # `letters` and `word` are two parameters that the function takes in. These values can be used as variables in the code
    for letter in word: # Loops through each letter in the word
        if letter in letters: # If the letter is part of the correctly guessed letters,
            continue # ...it moves on to the next letter in the word.
        else: # Otherwise, 
            return False # ...it means we have not guessed all the letters, meaning that the function will return the value False and end the function
    
    return True # If the loop is complete, and all letters in the word have been checked, it means that there werent any letters that we haven't guessed
    # This means we can return the value True as we have guessed all the letters in the word.

# -------------------
# MAIN PROGRAM
# -------------------
# Repeats following code until either the player wins or runs out of attempts.
while won == False and attempts > 0:
    # Checks if all the letters are guessed before continuing. checkWord() will return True if all letters are guessed, otherwise it will return False.
    if checkWord(lettersGuessed, word): # If the player have guessed all the letters...
        won = True # that means the player has won, which means we set `won` to True.
        continue # `continue` skips to next loop to avoid running the code if the user has already won.
        # In the next loop, `won == False` is not true, and lives can not be zero otherwise this section of code wouldn't run,
        # meaning that it will break out of the loop and run the code for when the game has ended.
    
    # Iterates (loops) through each letter in the word
    for _, letter in enumerate(word):
        # `Enumerate()` function splits every item in a list into it's index (position in list), and it's value.
        # Since a string is a list of characters, we can apply the enumerate function to loop through every character in the string.
        # `_` is the index of the letter in the word. We don't need that, so to stop it from saving to a variable and using up memory, we put `_`.
        # `letter` is each letter in the word.
        if letter in lettersGuessed: # If the player has previously guessed a letter...
            print(letter, end="") # it prints the letter.
        else: # Otherwise...
            print("_", end="") # it prints a '_'.
        # `end=""` prevents it from printing it on a new line every print statement, as end="\n" by default. `\n` means new line (known as a newline character).
    
    print("\n") # Prints an empty line, which makes the game look better, and prevents things from being printed out on the same line as the hidden word (as we didn't end it with a newline character).
    print(f"You have {attempts} lives left") # Tells the player their amount of attempts left. `f""` simply means we can format the string, such as by including values using `{value}`.
    print(f"Wrong letters: {', '.join(lettersIncorrectlyGuessed)}") # Tells the player their incorrect guesses. `', '.join()` joins every item in a list with a comma.
    print("--------------------------------------") # Makes the game look nicer by seperating the information given from where the user has to type in their guess
    
    userInput = input(">") # This lets the user input their guess. It puts '>' right before their input it to make it clear to the user to type something.
    # Checks the length of the guess.
    if len(userInput) > 1: # If the length of the guess is greater than 1, that must mean they guessed a word, not a letter.
        if userInput == word: # If the user has guessed the correct word...
            print("Correct Word! Well Done!") # we tell them they won,
            won = True # we set won to True,
            continue # and we skip the rest of the code in the `While` loop. When it checks if won is False, it will see that the statement is False, moving on to the next part of the code.
        else:
            print("Invalid guess") # Otherwise we simply tell them that their guess is wrong,
            attempts -= 1 # we subtract an attempt,
            continue # and we skip the rest of the code.
    elif len(userInput) == 1: # If the guess is 1 letter long, it must mean their guess was an individual letter. (`elif` is `else` and `if` combined. Only found in Python. used when checking more than 1 thing at once)
        if userInput in word and userInput not in lettersGuessed: # If their guess matches a letter in the word that they have not guessed yet...
            lettersGuessed.append(userInput) # the letter gets added to the correctly guessed letters,
            print("Well Done! Correct letter") # we tell the user that they guessed correctly,
            continue # and we skip the rest of the code.
        elif userInput in word and userInput in lettersGuessed: # If the user guesses a letter they have already guessed correctly...
            print("You have already guessed this letter!") # we tell them so,
            continue # and we skip the rest of the code.
        else: # Otherwise it must mean they guessed incorrectly, so...
            if not (userInput in lettersIncorrectlyGuessed): # we first check that they have not already guessed this letter incorrectly to avoid duplicates while printing,
                lettersIncorrectlyGuessed.append(userInput) # (if they haven't already guessed this incorrect letter then we add it to `lettersIncorrectlyGuessed`)
            print("Invalid guess") # we tell them they have guessed incorrectly,
            attempts -= 1 # and we subtract an attempt.
            # We didn't put `continue` as it is the end of the code anyways.
    # If neither situation happens, it must mean that the player inputted nothing - they simply pressed enter.
    # If so nothing will happen and the `while` statement will simply repeat again
            

# For this code to run, the game must have ended, either because they have won, or because they have ran out of attempts - `while won == False and attempts > 0:`. 
if won: # If they win...
    print("You won!") # We tell them they have won.
elif attempts <= 0: # If not...
    print("You ran out of guesses :(") # We tell them that they ran out of guesses
    
# -------------------
# DISCLAIMER - Message about `wordlist.txt`
# -------------------
# This file has been shared to me through the internet. I have not gone through it to filter out words, so I can not be sure if there are any offensive
# words within it. I am not responsible for any offense caused, nor have I got any intention to offend to anyone through this program. If you happen
# to find any offensive words in the file, please contact me somehow and tell me about them so that I can remove them.

# -------------------
# FINAL MESSAGE
# -------------------
# Thank you for reading my program, I hope it has helped you to deepen your understanding of python and programming. If you have any tips or suggestions, please make sure
# to contact me about them, and I will get back to you as soon as I can.