import wolt

SERVICES = {
    'wolt': wolt,
}

# use: SERVICES['wolt'].register(...)

def choose(service_name: str):
    """
    Returns the service object associated with the given service name.

    Args:
        service_name: The name of the service.

    Returns:
        The service object associated with the given service name.

    Example:
        ```python
        service = choose("account_generator")
        ```
    """

    return SERVICES[service_name]