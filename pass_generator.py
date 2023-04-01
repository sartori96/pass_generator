"""Password Generator Project"""
import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PassGenerator:
    """"This class generate the password"""

    def __init__(self):
        self.many_letters = 0
        self.many_numbers = 0
        self.many_symbols = 0
        self.pass_list = []

    def input_parameter_password(self):
        """"This method read the user's input"""
        self.many_letters = int(input("How many letters would you like in your password?\n"))
        self.many_numbers = int(input("How many numbers would you like?\n"))
        self.many_symbols = int(input("How many symbols would you like?\n"))

    def generate_characters_password(self):
        """
        Picks random characters to generate the password
        :return: list
        """
        letters_password = [random.choice(LETTERS) for _ in (range(self.many_letters))]
        numbers_password = [random.choice(NUMBERS) for _ in (range(self.many_numbers))]
        symbols_password = [random.choice(SYMBOLS) for _ in (range(self.many_symbols))]

        self.pass_list = letters_password + numbers_password + symbols_password
        return self.pass_list

    def define_password(self):
        """
        Make the password less predictable by randomize they
        :return: str
        """
        random.shuffle(self.pass_list)
        _final_password = "".join(self.pass_list)
        return _final_password


if __name__ == "__main__":
    pass_generator = PassGenerator()
    pass_generator.input_parameter_password()
    pass_list = pass_generator.generate_characters_password()
    print("Your new password is: " + pass_generator.define_password())
