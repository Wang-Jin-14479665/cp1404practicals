"""
Emails
Estimate: 20 minutes
Actual:   minutes
"""


def main():
    emails = {}

    user_email = input('Email: ').strip()
    while user_email != "":
        name = extract_name(user_email)  # A function that extracts the first half of the name from the email
        name_check = input(f"Is your name {name}? (Y/n): ").upper()
        if name_check not in ("Y", "YES", ""):
            name = input("Name: ")

        emails[name] = user_email
        user_email = input('Email: ').strip()

    for name, email in emails.items():
        print(f"{name} ({email})")


def extract_name(user_email):
    """This function extracts the name of the first half of the entered email"""
    parts = user_email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


main()