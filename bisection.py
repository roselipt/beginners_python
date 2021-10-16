#  Bisection search

target = int(input("Please pick a number: "))

print("Got it! Now the amazing Guess-mo Machine will guess your number!")

lower_bound = 0
upper_bound = 100
guess = 50
attempt = 0
count_words = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
found = False

while not found :
    print(" (rubbing forehead) ... Guess-mo's", count_words[attempt], "guess is", guess, "!")
    attempt +=1
    if guess == target :
        print("\nDat's it")
        found = True
    elif (guess < target) :
        lower_bound = guess
        print("Too low! Next guess will bisect", lower_bound, "and", upper_bound)
    else :
        upper_bound = guess
        print("Too high! Next guess will bisect", lower_bound, "and", upper_bound)
    guess = int(lower_bound + ((upper_bound - lower_bound)/2))
    
print("Guess-mo has done it again, guessing", guess, "in", attempt, "steps!")    
        
#        found = (input("You want me to change found?") == "y")
    
print("And that is show business.")

