import random 
from scoring import calculate_final_score
#new comment2
def guess_the_number_game():
    """
    A simple guessing game where the player tries to guess a secret number
    within a certain range, getting hints along the way.
    """
    print("-------------------------------------")
    print("Welcome to Guess the Number Game!")
    print("-------------------------------------")

 
    secret_number = random.randint(1, 100)
    attempts = 0 
    max_attempts = 10 

    print(f"I've picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")


    while attempts < max_attempts:
        try:
       
            guess_str = input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: ")
            guess = int(guess_str) 

           
            if not (1 <= guess <= 100):
                print("Please guess a number between 1 and 100.")
                continue 

            attempts += 1 

            # --- Check the Guess ---
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                # Correct guess!
                print(f"\nCongratulations, {guess} is the correct number!")
                print(f"You guessed it in {attempts} attempts.")
                # --- Using the extra feature from scoring.py ---
                final_score = calculate_final_score(attempts, max_attempts)
                print(f"Your Final Score: {final_score} points!")
                
                return # End the function (and game)

        except ValueError:
            # Handle cases where input isn't a number
            print("Invalid input. Please enter a whole number.")

    # --- Game Over (if loop finishes without correct guess) ---
    print("\n-------------------------------------")
    print("Game Over! You ran out of attempts.")
    print(f"The secret number was {secret_number}.")
    print("-------------------------------------")

# --- Start the game ---
if __name__ == "__main__":
    guess_the_number_game()
