import random

def pass_generator(length):
    if length > 8:
        print("Max length of password must be 8")
        return

    lowercase_letters = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
    uppercase_letters = [chr(i) for i in range(65, 91)]   # 'A' to 'Z'
    digits = [chr(i) for i in range(48, 58)]              # '0' to '9'
    specials = list('!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?`~') # Special characters

    # Combine all character arrays
    all_characters = lowercase_letters + uppercase_letters + digits + specials

    print("Here we generate a new and secure password for you....")
    user_letters = int(input("1. How many letters do you want in the password?\n"))
    user_symbols = int(input("2. How many symbols do you want in the password?\n"))
    user_numbers = int(input("3. How many numbers do you want in the password?\n"))

    if user_letters + user_symbols + user_numbers != length:
        print(f"Total characters (letters + symbols + numbers) must equal {length}.")
        return

    password = []

    # Adding user-specified number of each type of character
    for _ in range(user_letters):
        password.append(random.choice(lowercase_letters + uppercase_letters))

    for _ in range(user_symbols):
        password.append(random.choice(specials))

    for _ in range(user_numbers):
        password.append(random.choice(digits))

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    # Convert list to string and return
    generated_password = ''.join(password)
    print(f"Generated Password: {generated_password}")

def main():
    length = int(input("Enter the desired length of the password (max 8): "))
    pass_generator(length)

if __name__ == "__main__":
    main()
