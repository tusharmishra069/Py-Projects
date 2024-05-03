import random
import string

# Generate a random email address
def generate_email():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for i in range(10)) + '@gmail.com'

# Generate a random password
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(12))

# Generate a test email address and password
email = generate_email()
password = generate_password()

print(f"Generated email: {email}")
print(f"Generated password: {password}")