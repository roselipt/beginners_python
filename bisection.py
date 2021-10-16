#  Bisection search

target = int(input("Please pick a number: "))

print("Got it! Now the amazing Guess-mo Machine will guess your number!")

attempt = 0
lower_bound = 0
upper_bound = 100
found = False
guess = 50

while not found :
    print(" (rubbing forehead) ... Guess-mo's first guess is", guess, "!")
    attempt +=1
    if guess == target :
        print("Dat's it")
        found = True
    elif (guess < target) :
        lower_bound = guess
    else :
        upper_bound = guess
    print(guess, "isn't it and new range is", lower_bound, "to", upper_bound)
    guess = int(lower_bound + ((upper_bound - lower_bound)/2))
    
print("Guess-mo has done it again, guessing", guess, "in", attempt, "steps!")    
        
#        found = (input("You want me to change found?") == "y")
    
print("And that is show business.")

