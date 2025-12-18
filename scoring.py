# scoring.py

def calculate_final_score(attempts_taken, max_attempts):
    """
    Calculates a score based on efficiency.
    Example: 10/10 attempts used = 100 points, 1/10 used = 1000 points.
    """
    if attempts_taken == 0:
        return 0
    
    # Base score of 1000, subtracting 100 for every attempt used
    score = (max_attempts - (attempts_taken - 1)) * 100
    return score
