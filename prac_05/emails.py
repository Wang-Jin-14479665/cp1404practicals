"""
Emails
Estimate: 20 minutes
Actual:   minutes
"""


def main():
    emails = {}

    user_email = input('Name: ')
    while user_email != "":
        name = extract_name()  # A function that extracts the first half of the name from the email
        name_check = input(f"Is your name{name}? (Y/n):").upper()
        if name_check not in ("Y", "YES", ""):
            name = input("Name: ")

        emails[user_email] = name
        user_email = input('Name: ')

    for name, email in emails.items():
        print(f"{name} ({email})")


def extract_name():
    """This function extracts the name of the first half of the entered email"""


main()