import re

class Regex:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class RegexRegistry:
    def __init__(self):
        self.registry = {}

    def register(self, name: str, patterns: dict):
        if name in self.registry:
            raise ValueError(f"{name} already exists in the registry!")
        self.registry[name] = Regex(**patterns)

    def query(self, name: str, pattern_type: str):
        """Queries for a specific regex pattern type under a given name."""
        if name not in self.registry:
            raise ValueError(f"{name} does not exist in the registry!")
        regex_object = self.registry[name]
        return getattr(regex_object, pattern_type, None)

regex_registry = RegexRegistry()