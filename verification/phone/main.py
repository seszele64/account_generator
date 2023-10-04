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
    ):

    return order.sms[0].activation_code

