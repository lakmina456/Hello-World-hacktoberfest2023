import random


secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
       
        guess = int(input("Enter your guess: "))
        attempts += 1

       
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")

