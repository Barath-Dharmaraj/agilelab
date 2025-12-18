import time

def run_quiz():
    """A simple interactive quiz game."""
    score = 0
    total_questions = 3

    print("Welcome to the Basic Python Quiz!")
    time.sleep(1)
    print(f"You will be asked {total_questions} questions.")
    print("Good luck!\n")
    time.sleep(1.5)

    # --- Question 1 ---
    print("Question 1:")
    answer1 = input("What keyword is used to define a function in Python? (a) def, (b) func, (c) define: ").strip().lower()

    if answer1 == 'a' or answer1 == 'def':
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is 'def'.")
    print("-" * 20)
    time.sleep(1)

    # --- Question 2 ---
    print("Question 2:")
    answer2 = input("Which data type is immutable? (a) list, (b) dict, (c) tuple: ").strip().lower()

    if answer2 == 'c' or answer2 == 'tuple':
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is 'tuple'.")
    print("-" * 20)
    time.sleep(1)

    # --- Question 3 ---
    print("Question 3:")
    answer3 = input("What built-in function is used to print output to the console? ").strip().lower()

    if answer3 == 'print':
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is 'print'.")
    print("-" * 20)
    time.sleep(1)

    # --- Final Results ---
    print("\nQuiz finished!")
    print(f"Your final score is: {score}/{total_questions}")
    
    if score == total_questions:
        print("Excellent job! You got all questions right.")
    elif score >= total_questions / 2:
        print("Good effort! You passed.")
    else:
        print("Keep practicing your Python basics.")

# This line ensures the function runs when the script is executed
if __name__ == "__main__":
    run_quiz()
