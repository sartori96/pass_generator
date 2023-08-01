import random

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'

class PassGenerator:
    def __init__(self):
        self.many_letters = 0
        self.many_numbers = 0
        self.many_symbols = 0

    def input_parameter_password(self):
        self.many_letters = int(input("How many letters would you like in your password?\n"))
        self.many_numbers = int(input("How many numbers would you like?\n"))
        self.many_symbols = int(input("How many symbols would you like?\n"))

    def generate_characters_password(self):
        letters_password = random.choices(LETTERS, k=self.many_letters)
        numbers_password = random.choices(NUMBERS, k=self.many_numbers)
        symbols_password = random.choices(SYMBOLS, k=self.many_symbols)

        password_chars = letters_password + numbers_password + symbols_password
        random.shuffle(password_chars)
        return ''.join(password_chars)

    def __str__(self):
        return "Your new password is: " + self.generate_characters_password()

if __name__ == "__main__":
    pass_generator = PassGenerator()
    pass_generator.input_parameter_password()
    print(pass_generator)
