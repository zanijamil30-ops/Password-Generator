# password_generator.py
import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generate a random password.
    Parameters:
        length (int): desired password length (min 4, max 100)
        use_uppercase (bool): include uppercase letters
        use_digits (bool): include digits
        use_symbols (bool): include punctuation symbols
    Returns:
        str: generated password
    """
    # sanitize length
    try:
        length = int(length)
    except (TypeError, ValueError):
        length = 12

    if length < 4:
        length = 4
    if length > 100:
        length = 100

    # base charset: lowercase always included
    charset = list(string.ascii_lowercase)
    if use_uppercase:
        charset += list(string.ascii_uppercase)
    if use_digits:
        charset += list(string.digits)
    if use_symbols:
        # remove whitespace-like punctuation if any and ambiguous chars if desired
        symbols = [c for c in string.punctuation if c not in (' ', '`', '"')]
        charset += symbols

    # ensure at least one character from each requested category for stronger passwords
    password_chars = []
    password_chars.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice([c for c in string.punctuation if c not in (' ', '`', '"')]))

    # fill the rest
    while len(password_chars) < length:
        password_chars.append(random.choice(charset))

    # shuffle to avoid predictable sequences
    random.shuffle(password_chars)
    password = ''.join(password_chars[:length])
    return password

# No top-level UI code or Gradio. This file is safe to import from Flask.
if __name__ == "__main__":
    # Quick local test when running this module directly
    print("Example password:", generate_password(12, True, True, True))

