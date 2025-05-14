import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_strong_password(password):
    if len(password)<9:
        return False
    has_upper = any(char.isupper() for char in password)
    has_alpha = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_alpha and has_digit