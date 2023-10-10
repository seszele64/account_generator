# what fields are there -> types of data
import re
from dataclasses import dataclass
import random
import string

class CharacterLimits:

    def __init__(self, max, min):
        self.max = max
        self.min = min

# random string generator
class RandomStringManager(
    ):
    def __init__(self, length=None, uppercase=None, lowercase=None, numbers=None, special=None):
        self.length = CharacterLimits(*length)
        self.uppercase = CharacterLimits(*uppercase)
        self.lowercase = CharacterLimits(*lowercase)
        self.numbers = CharacterLimits(*numbers)
        self.special = CharacterLimits(*special)

    # call -> reproduces string
    def __call__(self):
        return self.generate_random_string()

    # Function to generate random characters of chosen type an length (limits)
    def generate_random_characters(self, characters, length):
        return ''.join(random.choices(characters, k=length))

    # Function to generate uppercase characters
    def generate_uppercase(self):
        return self.generate_random_characters(string.ascii_uppercase, self.uppercase.min)
        # return ''.join(random.choices(string.ascii_uppercase, k=self.uppercase.min))
    
    # Function to generate lowercase characters
    def generate_lowercase(self):
        # return ''.join(random.choices(string.ascii_lowercase, k=self.lowercase.min))
        return self.generate_random_characters(string.ascii_lowercase, self.lowercase.min)

    # Function to generate numbers
    def generate_numbers(self):
        # return ''.join(random.choices(string.digits, k=self.numbers.min))
        return self.generate_random_characters(string.digits, self.numbers.min)

    # Function to generate special characters
    def generate_special(self):
        # no spaces
        special_characters = random.choices(string.punctuation.replace(' ', ''), k=self.special.min)
        
        while any(char in special_characters for char in ['"', "'", '\\']):
            special_characters = random.choices(string.punctuation.replace(' ', ''), k=self.special.min)

        return ''.join(special_characters)
    

    # Function to generate a random string based on character type counts
    def generate_random_string(self):

        return (
            self.generate_uppercase() +
            self.generate_lowercase() +
            self.generate_numbers() +
            self.generate_special()
        )
    
    # shuffle the string
    def shuffle(self, string):
        return ''.join(random.sample(string, len(string)))
    
    # add random characters to the end of the string
    def add_random_character(self, string):
        return string + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    
    # length adjuster

    def adjust_length(self, string):
        while not self.check_length(string):
            if len(string) < self.length.min:
                string += self.generate_random_string()
            elif len(string) > self.length.max:
                string = string[:self.length.max]
                break
        return string



    def check_length(self, string):
        return self.length.min <= len(string) <= self.length.max

    # generate random string that matches the limits
    def generate(self):
        # Generate random password
        password = self.generate_random_string()

        # Shuffle the password
        password = self.shuffle(password)

        # adjust length
        password = self.adjust_length(password)

        return password
    

# call -> reproduces string
def get_random_string(length=(8, 16), uppercase=(1, 4), lowercase=(1, 4), numbers=(1, 4), special=(1, 4)):
    return RandomStringManager(
        length=length,
        uppercase=uppercase,
        lowercase=lowercase,
        numbers=numbers,
        special=special
    ).generate()