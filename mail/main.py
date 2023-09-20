from yopmail import Yopmail
from mail.links import *


# initialize yopmail object
yopmail = Yopmail('d.skoliba')
# get mail ids
mail_ids = yopmail.get_mail_ids()
# read last mail
mail = yopmail.get_mail_body(mail_ids[0])
# find link in mail
service = ServiceRegistry.get_service('wolt')
link = service.get_verification_link(mail)
print(link)