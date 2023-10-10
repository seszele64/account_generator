from .registry import regex_registry

def register_services():
    # Register your regex patterns for each service
    regex_registry.register('wolt', {'verification': r'https://wolt.com/me/magic_login[^"]*', 'login': r'https://wolt.com/me/magic_login[^"]*', 'register': r'https://wolt.com/me/magic_login[^"]*'})
    
    print("Regexes registered.")