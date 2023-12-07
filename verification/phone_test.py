# testing phone service

from phone import *

phone_manager = PhoneManager()
# get phone number
# phone_number = phone_manager.get_phone_number()
# print(phone_number)

# make order
order = phone_manager.make_order(Country.CAMEROON, ActivationProduct.FACEBOOK)
print(order)

# get phone number
phone_number = phone_manager.get_phone_number()
print(phone_number)

# cancel order
phone_manager.cancel_order(order)

print("Voila!")