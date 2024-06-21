import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    number_pick = int(input("How many quick picks? "))
    for i in range(number_pick):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    picks = []
    while len(picks) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in picks:
            picks.append(number)
    picks.sort()  # displayed in sorted (ascending) order
    return picks

main()
