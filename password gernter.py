# import string
# import secrets
# from venv import create
#
#
# def  Create_pw(pw_lenght=12, pw_length=None):
#     letters = string.ascii_letters
#     digits = string.digits
#     special_chars = string.punctuation
#
#     alphabet = letters + digits + special_chars
#     pwd = ''
#     pw_strong=False
#
#     while  not pw_strong:
#
#         while not pw_strong:
#             pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))
#
#             # Ensure password contains at least one special character and at least two digits
#             if any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2:
#                 pw_strong = True
#
#             return pwd
#         if __name__ == "__main__":
#             print("Generated Secure Password:", create_pw())
import string
import secrets

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))

        # Ensure password contains at least one special character and at least two digits
        if any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2:
            pw_strong = True

    return pwd

# Ensuring correct execution
if __name__ == "__main__":
    print("Generated Secure Password:", create_pw())