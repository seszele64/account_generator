# what fields are there -> types of data
import re
from dataclasses import dataclass
import random
import string

class RandomStringManager:
    def __init__(self, length_range=(12, 16), uppercase_count=(1,2), lowercase_count=(1,2), numbers_count=(1,2), special_count=(1,2)):
        self.length_range = length_range
        self.uppercase_count = uppercase_count
        self.lowercase_count = lowercase_count
        self.numbers_count = numbers_count
        self.special_count = special_count

# random string generator
    def generate(self):
        length = random.randint(*self.length_range)
        uppercase_chars = ''.join(random.choices(string.ascii_uppercase, k=random.randint(*self.uppercase_count)))
        lowercase_chars = ''.join(random.choices(string.ascii_lowercase, k=random.randint(*self.lowercase_count)))
        numbers_chars = ''.join(random.choices(string.digits, k=random.randint(*self.numbers_count)))
        special_chars = ''.join(random.choices(string.punctuation.replace(' ', ''), k=random.randint(*self.special_count)))

        combined_chars = uppercase_chars + lowercase_chars + numbers_chars + special_chars
        password = ''.join(random.sample(combined_chars, length))
        return password

