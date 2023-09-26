# what fields are there -> types of data
import re
from dataclasses import dataclass
import random
import string

class CharacterLimits:

    max: int = None
    min: int = None

    def __init__(self, max=None, min=None):
        self.max = max
        self.min = min

class Limits:

    length: CharacterLimits = None
    uppercase: CharacterLimits = None
    lowercase: CharacterLimits = None
    numbers: CharacterLimits = None
    special: CharacterLimits = None

    def __init__(self, length=None, uppercase=None, lowercase=None, numbers=None, special=None):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special = special

# random string generator
class RandomString(
    ):
    
    def __init__(self, limits):
        self.limits: Limits = limits

    # call -> reproduces string
    def __call__(self):
        return self.generate_random_string()

    # Function to generate random characters of chosen type an length (limits)
    def generate_random_characters(self, characters, length):
        return ''.join(random.choices(characters, k=length))

    # Function to generate uppercase characters
    def generate_uppercase(self):
        return self.generate_random_characters(string.ascii_uppercase, self.limits.uppercase.min)
        # return ''.join(random.choices(string.ascii_uppercase, k=self.limits.uppercase.min))
    
    # Function to generate lowercase characters
    def generate_lowercase(self):
        # return ''.join(random.choices(string.ascii_lowercase, k=self.limits.lowercase.min))
        return self.generate_random_characters(string.ascii_lowercase, self.limits.lowercase.min)

    # Function to generate numbers
    def generate_numbers(self):
        # return ''.join(random.choices(string.digits, k=self.limits.numbers.min))
        return self.generate_random_characters(string.digits, self.limits.numbers.min)

    # Function to generate special characters
    def generate_special(self):
        # no spaces
        special_characters = random.choices(string.punctuation.replace(' ', ''), k=self.limits.special.min)
        
        while any(char in special_characters for char in ['"', "'", '\\']):
            special_characters = random.choices(string.punctuation.replace(' ', ''), k=self.limits.special.min)

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

    ## check length
    def check_length(self, string):

        if len(string) < self.limits.length.min:
            return False
        elif len(string) > self.limits.length.max:
            return False
        else:
            return True

    ## adjust length helper
    def adjust_length_helper(self, string):
        if len(string) < self.limits.length.min:
            return string + self.generate_random_string()
        elif len(string) > self.limits.length.max:
            return string[:-1].join(random.sample(string[:-1], len(string[:-1])))
        else:
            return string

    def adjust_length(self, string):

        while not self.check_length(string):
            string = self.adjust_length_helper(string)
        return string
        
    # generate random string that matches the limits
    def generate(self):
        # Generate random password
        password = self.generate_random_string()

        # Shuffle the password
        password = self.shuffle(password)

        # adjust length
        password = self.adjust_length(password)

        return password

