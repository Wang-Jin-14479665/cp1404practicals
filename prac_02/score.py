"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)
    new_score = random.randint(1, 100)
    new_result = evaluate_score(new_score)
    print(new_result)


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


main()
