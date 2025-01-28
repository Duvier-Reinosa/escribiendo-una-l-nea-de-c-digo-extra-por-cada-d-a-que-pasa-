import secrets, string, sys
from termcolor import colored
def gen_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    password = gen_password(length)
    print(colored("🚀 Secure Password Generator 🚀", "cyan", attrs=["bold"]))
    print(colored(f"Generated password ({length} characters):", "green", attrs=["bold"]))
    print(colored(password, "yellow"))