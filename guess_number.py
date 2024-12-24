import random

number_to_guess = random.randint(1,10)
attempts = 0

while True:
    guess = int(input("guess the number (1-10): "))
    attempts += 1
    
    if guess == number_to_guess:
        print(f"congratulations you guessed the right number in {attempts} attempts")
        break
    elif guess < number_to_guess:
        print(f"the number is bigger than your guess, guess attempts: {attempts}")
    else:
        print(f"the number is smaller than your guess, guess attempts: {attempts}")
