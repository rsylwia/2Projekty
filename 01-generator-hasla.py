import sys
import random
import string

password = []
characters_left = -1
password_length = int(input("Jak długie ma być hasło? "))

def update_characters_left(number_of_characters):
    global characters_left
    if number_of_characters > characters_left or number_of_characters < 0:
        print("Liczba znaków spoza przedziału 0, ", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostałych znaków: ", characters_left)

if password_length < 5:
    print("Hasło musi mieć min. 5 znaków. Spróbuj jeszcze raz.")
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostałych wykorzystane. Hasło zostanie usuzpełnione małymi literami.")
    lowercase_letters += characters_left

print()
print("Długość hasła: ", password_length)
print("Małe lister: ", lowercase_letters)
print("Duże litery: ", uppercase_letters)
print("Znaki specjalne: ", special_characters)
print("Cyfry: ", digits)

for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
random.shuffle(password)
print("Twoje hasło to: ", "".join(password))