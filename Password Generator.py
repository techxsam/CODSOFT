import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for good security.")
        return None

    # Define possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Use random choices to generate password
    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()