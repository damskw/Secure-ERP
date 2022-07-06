import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    random_id = []
    uppercases = string.ascii_uppercase
    lowercases = string.ascii_lowercase
    for special_chars in range(number_of_special_chars):
        special_char = random.choice(allowed_special_chars)
        random_id.append(special_char)
    for digits in range(number_of_digits):
        digit = random.randint(0, 9)
        random_id.append(digit)
    for capital_letters in range(number_of_capital_letters):
        capital_letter = random.choice(uppercases)
        random_id.append(capital_letter)
    for small_letters in range(number_of_small_letters):
        small_letter = random.choice(lowercases)
        random_id.append(small_letter)
    random.shuffle(random_id)
    random_id = ''.join(str(element) for element in random_id)
    return random_id