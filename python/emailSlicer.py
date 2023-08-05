def email_slicer(email):
    at_index = email.find('@')  # Get the index of '@' in the email

    if at_index == -1:  # if '@' is not found
        return None

    # Slice the email
    username = email[:at_index]
    domain = email[at_index + 1:]

    return username, domain

email = input("Enter your email: ")
result = email_slicer(email)

if result:
    print(f"Username: {result[0]}")
    print(f"Domain: {result[1]}")
else:
    print("Invalid email.")
