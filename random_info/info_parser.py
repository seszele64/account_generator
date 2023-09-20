import re

def parse_address(address: str) -> tuple:
    pattern = r'^(\d+)\s+(.+)'
    if not (match := re.match(pattern, address)):
        raise ValueError(f'Invalid address: {address}')
    street_number = match[1]
    street_name = match[2]
    return street_name, street_number

# parse name
def parse_name(name: str) -> tuple:
    pattern = r'^(\w+) (\w+)$'
    if not (match := re.match(pattern, name)):
        raise ValueError(f'Invalid name: {name}')
    first_name, last_name = match[1], match[2]
    return first_name, last_name