"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Peřinová
email: perinova.petra@seznam.cz
"""
import random

def generate_secret_number():
    digits = list("123456789")  # Possible first digits (cannot be 0)
    first_digit = random.choice(digits)
    remaining_digits = list("0123456789")
    remaining_digits.remove(first_digit)
    secret = first_digit + "".join(random.sample(remaining_digits, 3))
    return secret

def is_valid_guess(guess, previous_guesses):
    line = "-" * 35
    guess = guess.strip()  # Odstraní mezery na začátku a na konci
    if not guess.isdigit():  # Zkontroluje, jestli jsou všechny znaky číslice
        print(line)
        print("Invalid input! Use digits only.")
        print(line)
        return False
    if len(guess) != 4:  # Zkontroluje, jestli má číslo 4 cifry
        print(line)
        print("The number must have exactly 4 digits.")
        print(line)
        return False
    if guess[0] == '0':  # Zkontroluje, jestli číslo nezačíná nulou
        print(line)
        print("The number cannot start with 0.")
        print(line)
        return False
    if guess in previous_guesses:  # Zkontroluje, jestli už tento tip nebyl zadán
        print(line)
        print("You've already tried this number!")
        print(line)
        return False
    return True

def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)  # Počet "bulls"
    cows = sum(1 for g in guess if g in secret) - bulls  # Počet "cows" bez "bulls"
    return bulls, cows

def print_result(bulls, cows):
    line = "-" * 35
    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    print(line)
    print(f"{bulls} {bulls_text}, {cows} {cows_text}")
    print(line)

def main():
    line = "-" * 35
    print("Hi there!")
    print(line)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(line)
    secret_number = generate_secret_number()
    attempts = 0
    previous_guesses = set()  # Uchování předchozích tipů
    
    while True:
        print("Enter a number:")
        print(line)
        guess = input(">>> ").strip()
        if not is_valid_guess(guess, previous_guesses):
            continue
        
        previous_guesses.add(guess)  # Uložíme číslo, aby se neopakovalo
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print_result(bulls, cows)
        
        if bulls == 4:
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print(line)
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()


