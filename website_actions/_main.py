# # ---------------------------------- imports --------------------------------- #

# import sys

# # # Add the parent directory to the sys.path list
# sys.path.append(".")
# from browser.manager import MyBrowser as driver
# from browser.actions import WebActions

# # from enums import ServiceEnum

# # --------------------------------- services --------------------------------- #

# from dataclasses import dataclass

# @dataclass
# class ServiceData:
#     person: 'Person' = None
#     real_data: 'RealData' = None
#     phone: phone = None
#     email: email = None
#     password: password = None

# class Service:
    
#     def __init__(self, base_url, instructions, data):
#         self.name = self.__class__.__name__

#         self.base_url = base_url
#         self.instructions = instructions
#         self.data = ServiceData(**data)

#     def select_action(self):
#         self.print_actions()
#         action_index = int(input("Select action: "))
#         return self.actions[action_index]

#     def print_actions(self):
#         for i, action in enumerate(self.actions):
#             print(f"{i}: {action}")

#     def execute(self, **kwargs):

#         # select action
#         action = self.select_action()

#         # perform action
#         action.perform(
#             browser = driver,
#             **kwargs
#         )

#     def __repr__(self):
#         return f"Service(name={self.name}, actions={self.instructions})"
    
