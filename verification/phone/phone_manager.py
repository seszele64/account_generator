from .fivesim import FiveSim, Country, Operator, FiveSimError, ActivationProduct, Order, OrderAction

import logging
import os
from dotenv import load_dotenv

load_dotenv()

class PhoneManager(FiveSim):

    def __init__(self):
        # Initialize the parent class with the API key
        super().__init__(api_key=os.getenv("TOKEN"))
        self.order = None

    def make_order(self, country: Country, product: ActivationProduct) -> Order:
        """
        Makes an order for the given `country` and `product`.

        Args:
            country (Country): The country to make the order for.
            product (ActivationProduct): The product to make the order for.
            token (str): The API key to use for authentication. Defaults to the value of the 'TOKEN' environment variable.

        Returns:
            Order: The order that was made.

        Raises:
            FiveSimError: If an error occurs while making the order.

        Example:
            ```python
            order = make_order(Country.US, ActivationProduct.TINDER)
            print(order)
            ```
        """

        try:
            order = self.user.buy_number(
                country = country, operator=Operator.ANY_OPERATOR, product=product
            )
            
            self.order = order

        except FiveSimError as e:
            logging.error(e)
            raise e

        return order

    def get_phone_number(self) -> str:

        if self.order is None:
            raise Exception("You must make an order before getting a phone number.")

        return self.order.phone

    def get_verification_code(
            self,
            order: Order
        ) -> str:

        return order.sms[0].activation_code
    
    # cancel order
    def cancel_order(self, order: Order) -> None:
        """
        Cancels the given `order`.

        Args:
            order (Order): The order to cancel.

        Raises:
            FiveSimError: If an error occurs while cancelling the order.

        Example:
            ```python
            cancel_order(order)
            ```
        """

        try:
            self.user.order(OrderAction.CANCEL, order)
        except FiveSimError as e:
            logging.error(e)
            raise e

