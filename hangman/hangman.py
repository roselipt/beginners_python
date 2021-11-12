# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    done = True
    for letter in secret_word :
      if letter not in letters_guessed :
        done = False
        break
    return done
    #pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    space = "_ "

    for letter in secret_word :
      if letter in letters_guessed :
        guessed_word += letter
        guessed_word += " "
      else :
        guessed_word += space
    return guessed_word
    #pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available = ""
    for letter in alphabet :
      if letter not in letters_guessed :
        available += letter
    return available
    
def unique_letters(secret_word):
  """
  secret_word: string, the secret word the user is guessing
  return: int, number of unique letters in secret word
  """
  unique_letters = []
  for i in secret_word :
    if i not in unique_letters :
      unique_letters += i
  print("  ... just for buggin man:", unique_letters)
  return len(unique_letters)
  
def score_word(secret_word, guesses) :
  """
  secret_word: string, the secret word the user is guessing
  guesses: int, number of guesses remaining after word is completely guessed
  return: int, score for game 
  """
  pass


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print("Let's play a game of Hangman!")
    print("I'm thinking of a word that is", len(secret_word), "long.")
    
    #  While guesses remain: get guess and show result
    guessed = []
    guesses = 6
    warnings = 3
    win = False
    score = 0
    vowels = ['a', 'e', 'i', 'o', 'u']  #  Needed to keep score
    
    while guesses != 0 :
      #  Show number of guesses left
      if guesses > 1 :
        print("You have", guesses, " guesses left.")
      else :
        print("Just", guesses, "guess left!")
      #  Show letters available to guess
      print("Letters still available are", get_available_letters(guessed))
      #  Get guess from player
      guess = input(" Guess! One lower case letter only, please! ")
      print()

      #  Check if input is (single) letter, apply game rules.
      #  (Aside for later: I discovered some odd behavior when user entered two letters.
      #   Like 'ab' entered by accident would become 'a' and 'b' in list of guesses.
      #   Len == 1 solves the problem. But I still don't totally understand:
      #   Why += 'ab' adds the two separately and not together as list.append('ab') does.)
      if str.isalpha(guess) and len(guess) == 1 : 
        guess = str.lower(guess)
        #  Check if input is new (hasn't been guessed yet).
        if guess not in guessed :
          guessed += guess
          #  Check if guess is in word.
          if guess in secret_word :
            print(" Sweet guess!", end="")
          else :
            print("Oops! That letter is not in my word.", end='')
            #  Try ternary here later?
            if guess in vowels :
              print(" A wrong vowel costs 2 guesses!", end = '')
              guesses -= 2 
            else :
              guesses -= 1
      
        #  If guess is a repeat and warnings remain, take one warning away.
        elif warnings > 0 :
          print(guess, "Oops! You already guessed that letter.", end='')
          warnings -= 1
          print(" You have", warnings, "warnings left.", end= '')
        #  Else guess is repeat, no warnings remain, take one guess away.
        else :
          print("You've already guessed that letter. You have no warnings left so that costs a guess.", end='')
          guesses -= 1
      
      #  Input is not letter and warnings remain.
      elif warnings > 0 :
        warnings -= 1
        print("Oops! That is not a letter. You have", warnings, "warnings left.", end="")
      
      #  Input is not letter and no warnings remain. That costs a guess.
      else :
        print("Oops! That is not a letter! You have no warnings left so that costs a guess", end="")
        guesses -= 1

      #  Show guess at the end of every turn.
      #  This appears at the end of every line from the if ladder above.  
      print("  ", get_guessed_word(secret_word, guessed))

      #  Is the whole word guessed? 
      #  Break or print line to mark end of turn.
      if is_word_guessed(secret_word, guessed) :
        win = True
        print("YOU WIN!!!")
        break
      else :
        print("\n  --------\n")

    # End of while loop for turns

    if win : 
      print("Congratulations, you won!")
      score = guesses * unique_letters(secret_word)
      print("Your total score for this game is:", score)
    else : print(" You've run out of turns! Better luck next time!")
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    #  Strip spaces from my_word and convert to list
    my_word = [letter for letter in my_word if letter != ' ']          

    #  If lengths match proceed with check, else no match
    if len(my_word) == len(other_word) :
      #  Convert other_word to list    
      other_word = list(other_word)      
      #  Place blanks in other_word according to my_word
      for position in range(0, len(my_word)) :
        if my_word[position] == '_' :
          other_word[position] = '_'
      #  Compare the lists
      # print('From method our lists are:')
      # print(my_word)
      # print(other_word)
      return my_word == other_word
    
    else :  #  (Word lengths did not match.)
      return False

    #  The assignment gives a hint to use strip() which doesn't seem necessary to me
    #  and so makes me wonder if I'm missing something?
    # my_word = strip(my_word)
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist :
      if match_with_gaps(my_word, word) :
        print(word, end = " ")
    print()


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Let's play a game of Hangman!")
    print("I'm thinking of a word that is", len(secret_word), "long.")
    
    #  While guesses remain: get guess and show result
    guessed = []
    guesses = 6
    warnings = 3
    win = False
    score = 0
    vowels = ['a', 'e', 'i', 'o', 'u']  #  Needed to keep score
    
    while guesses != 0 :
      #  Show number of guesses left
      if guesses > 1 :
        print("You have", guesses, " guesses left.")
      else :
        print("Just", guesses, "guess left!")
      #  Show letters available to guess
      print("Letters still available are", get_available_letters(guessed))
      #  Get guess from player
      guess = input(" Guess! One lower case letter only, please! ")
      print()

      #  Check if input is (single) letter, apply game rules.
      #  (Aside for later: I discovered some odd behavior when user entered two letters.
      #   Like 'ab' entered by accident would become 'a' and 'b' in list of guesses.
      #   Len == 1 solves the problem. But I still don't totally understand:
      #   Why += 'ab' adds the two separately and not together as list.append('ab') does.)
      if str.isalpha(guess) and len(guess) == 1 : 
        guess = str.lower(guess)
        #  Check if input is new (hasn't been guessed yet).
        if guess not in guessed :
          guessed += guess
          #  Check if guess is in word.
          if guess in secret_word :
            print(" Sweet guess!", end="")
          else :
            print("Oops! That letter is not in my word.", end='')
            #  Try ternary here later?
            if guess in vowels :
              print(" A wrong vowel costs 2 guesses!", end = '')
              guesses -= 2 
            else :
              guesses -= 1
        #  If guess is a repeat and warnings remain, take one warning away.
        elif warnings > 0 :
          print(guess, "Oops! You already guessed that letter.", end='')
          warnings -= 1
          print(" You have", warnings, "warnings left.", end= '')
        #  Else guess is repeat, no warnings remain, take one guess away.
        else :
          print("You've already guessed that letter. You have no warnings left so that costs a guess.", end='')
          guesses -= 1
      #  If guess is secret symbol '*' for hints      
      elif guess == '*' :
        show_possible_matches(secret_word)

      #  Input is not letter and warnings remain.
      elif warnings > 0 :
        warnings -= 1
        print("Oops! That is not a letter. You have", warnings, "warnings left.", end="")
      
      #  Input is not letter and no warnings remain. That costs a guess.
      else :
        print("Oops! That is not a letter! You have no warnings left so that costs a guess", end="")
        guesses -= 1

      #  Show guess at the end of every turn.
      #  This appears at the end of every line from the if ladder above.  
      print("  ", get_guessed_word(secret_word, guessed))

      #  Is the whole word guessed? 
      #  Break or print line to mark end of turn.
      if is_word_guessed(secret_word, guessed) :
        win = True
        print("YOU WIN!!!")
        break
      else :
        print("\n  --------\n")

    # End of while loop for turns

    if win : 
      print("Congratulations, you won!")
      score = guesses * unique_letters(secret_word)
      print("Your total score for this game is:", score)
    else : print(" You've run out of turns! Better luck next time!")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)

    # print("Secret word is", secret_word)
    #  Set secret word for debugging.
    # secret_word = 'apple'
    # print(" But really now it's", secret_word)

    # hangman(secret_word)
    
    # #  Debugging code for finding matches
    # blanky = "a _ _ l e"
    # print("Blanky word is", blanky, " and match with gaps is", match_with_gaps(blanky, secret_word))
    # print()
    # print('And matching words are:')
    # show_possible_matches(blanky)

# print(secret_word)
# secret_word = 'apple'
# guessed = ['p']
# print("Now secret word is changed to", secret_word)
# print(" And guessed is", guessed)
# print("  Get_guessed_word for", guessed, "is:", get_guessed_word(secret_word, guessed))
# print("   Is_guessed for", guessed, "is", is_word_guessed(secret_word, guessed))
# print("    O and available letters is", get_available_letters(guessed))

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
