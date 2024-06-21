

MENU = "(G)et a valid score \n (P)rint result \n (S)how stars \n (Q)uit"

def main():
    score = None
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()

        elif choice == "P":
            if score is not None:
                result = evaluate_score(score)
                print(result)
            else:
                print("No score available. Please get a valid score first.")

        elif choice == "S":
            if score is None:
                print("No score available. Please get a valid score first.")
            else:
                print("*" * score)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Bye!")


def validate_score():
    """Verify that the scores entered are within the range"""
    score = int(input("Enter score:"))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = int(input("Enter score:"))
    return score

def evaluate_score(score):
    """The result is given according to the interval of achievement"""
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
