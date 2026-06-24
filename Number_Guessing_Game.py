import random

print("===== Number Guessing Game =====")

while True:
    
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Try Again.")

            elif guess > secret_number:
                print("Too High! Try Again.")

            else:
                print(f"\n🎉 Congratulations!")
                print(f"You guessed the number {secret_number} correctly.")
                print(f"Attempts Taken: {attempts}")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        break