"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_of_month = int(input("How many months? "))

    for month in range(1, numbers_of_month + 1):
        # Change the line that gets the income input so that it uses an f-string
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(numbers_of_month, incomes)


def print_report(numbers_of_month, incomes):
    """This function will print report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, numbers_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
