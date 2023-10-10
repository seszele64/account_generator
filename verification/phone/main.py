from fivesim import FiveSim, Country, Operator, FiveSimError, ActivationProduct, Order

import logging
import os
from dotenv import load_dotenv

load_dotenv()

def get_phone_number(
            country: Country,
            product: ActivationProduct,
            token = os.getenv("TOKEN")
            ) -> str:
    """
    Buys a phone number from FiveSim for the given `country` and `product`.

    Args:
        country (Country): The country to buy the phone number for.
        product (ActivationProduct): The product to buy the phone number for.
        token (str): The API key to use for authentication. Defaults to the value of the 'TOKEN' environment variable.

    Returns:
        str: The phone number that was bought.

    Raises:
        FiveSimError: If an error occurs while buying the phone number.

    Example:
        ```python
        phone_number = get_phone_number(Country.US, ActivationProduct.TINDER)
        print(phone_number)
        ```
    """
    client = FiveSim(api_key=token)

    try:
        result = client.user.buy_number(
            country=country,
            operator=Operator.ANY_OPERATOR,
            product=product,
        )

    except FiveSimError as e:
        logging.error(e)
        raise e

    return result.phone

def get_verification_code(
        order: Order
    ) -> str:
    """
    Gets the verification code for the given `order`.

    Args:
        order (Order): The order to get the verification code for.

    Returns:
        str: The verification code.

    Example:
        ```python
        order = client.user.get_order_by_id(order_id)
        verification_code = get_verification_code(order)
        print(verification_code)
        ```
    """
    return order.sms[0].activation_code