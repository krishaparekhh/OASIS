import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        print("Error: At least one character type must be selected. Defaulting to letters.")
        character_set = string.ascii_letters
    
    return "".join(random.choice(character_set) for _ in range(length))

def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
