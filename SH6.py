def hang_man(character, word):
    """
    This function allows to return the list of indexes found for the character in the word.
    """
    position = []
    for i in range(len(word)):
        if word[i] == character:
        		position.append(i)
    return position


if __name__ == '__main__':
  	# prompt for Player 1 to input the word
    word = input("(Player 1) Please enter the word: ").upper()
    while not word.isalpha(): # checks if word only contains values from a-z and no special characters
      	print("Invalid input. Please enter a valid word.")
      	word = input("(Player 1) Please enter a word which only contains characters from a-z: ")
    num_of_unique_char = len(set(word))
    
    # prompt for Play 1 to input the number of guesses
    guesses = input("(Player 1) Please enter the number of guesses allowed: ")
    while not guesses.isnumeric() or int(guesses) < num_of_unique_char or int(guesses)>30: # checks if the player input is a valid integer, greater than the minimum amount of guesses to win and less than 30
      	print(f'Invalid input. Please enter an integer between {num_of_unique_char} and 30, inclusive.')
      	guesses = input('(Player 1) Please enter the number of guesses: ')
    guesses = int(guesses)
    misses = []  # array to store missed guessed char
    word_array = list(word)
    progress = ["_"] * len(word) 
		
    # print the word (masked) and the number of guesses to the console for Player 2 to start playing
    print("=" * 50)
    print("WORD: ", ' '.join(progress))
    print("GUESSES LEFT: ", guesses)

    # starting the guessing loop for Player 2 based on the number of guesses allowed
    for i in range(1, guesses + 1):
        guessed_char = input(f'(Player 2) Please enter guess #{i}: ').upper()[0]
        # validate character input
        while not guessed_char.isalpha():
            print("Invalid input. Please enter a character from a-z.")
            guessed_char = input(f'(Player 2) Please enter guess #{i} again with valid character: ').upper()[0] # only take the first character from the input string

        # if user already guessed the character before, allow user to try again with another character
        if guessed_char in progress or guessed_char in misses:
          	guessed_char = input(f'(Player 2) You have already guessed the character "{guessed_char}". Please enter another character: ').upper()[0] # only take the first character from the input string
        
        # call function to return the found indexes in the word
        pos = hang_man(guessed_char, word)

        if len(pos) != 0:  # if indexes are found, replace _ with the guessed char
            print("Correct!")
            for p in pos:
                progress[p] = guessed_char
        else:  # if indexes are not found, add the guessed char to the misses list
            print("Incorrect. Letter is not in the word")
            misses.append(guessed_char)

        # print the word progress, the misses list and the number of guesses left
        print("WORD: ", ' '.join(progress))
        print("MISSES: ", ','.join(misses))
        print("GUESSES LEFT: ", guesses-i)
        print("=" * 50)
				
        # if all the blanks in the progress are filled, inform that user has won. 
        if "_" not in progress:
            print("Congrats! You win!")
            break
            
        