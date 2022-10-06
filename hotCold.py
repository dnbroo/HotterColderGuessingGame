import random

def closeOrFar(num, guess, lastGuess):
    curr = abs(num - guess)

    prev = abs(num - lastGuess)

    if curr < prev:
        print("Getting Hotter! :)\n")

    if curr > prev:
        print("Getting Colder! :(\n")

    if curr == prev:
        print("Your still the same distance away.")


num = random.randint(1,100)

guess = 0
count = 0
lastGuess = -1

print("Welcome to the Number guessing game!\nGo ahead and try to guess a number between 1 and 100.\n\n\n")


while guess != num:

    print("What is your guess?")
    guess = int(input())

    #print("Current guess: " + str(guess) + ". Your last guess: " + str(lastGuess) + "\n")

    count += count

    if guess == lastGuess:
        print("You've already guessed that!\n\n")
        continue

    if guess == num:
        break

    if lastGuess == -1:
        print("That's not quite it. Try Again!")
        lastGuess = guess
        continue

    closeOrFar(int(num), int(guess), int(lastGuess))
    lastGuess = guess


print("\n\n\nCongrats!!\n\nYou have guess the number!!\n\n")
