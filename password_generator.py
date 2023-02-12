import random
import string

def generate_password(length=24, chars=string.ascii_letters + string.digits + string.punctuation): # Set the values to a default if they aren't added
    #Generate a password with the specified size and charset
    return "".join(random.choice(chars) for _ in range(length))

# Generate it
password = generate_password(2)

# Print it out
print(f"Random password: {password}")
