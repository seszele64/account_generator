from mail import MailManager, MailLinkExtractor

def test_link_inbox():
    """
    Tests the `check_link_inbox` function.
    """
    username = 'martyna.adamczyk'

    mail = MailManager(username)
    service = MailLinkExtractor.ServiceLinks.get_service('WOLT')
    regex_pattern = service.verification.value
    
    # get link
    return mail.check_link_inbox(regex_pattern)

# create mail address
def test_create_mail_address():
    """
    Tests the `create_mail_address` function.
    """
    name = 'martyna.adamczyk'
    mail = MailManager(name)
    return mail.create_mail_address()

if __name__ == "__main__":
    print(test_create_mail_address())
    print(test_link_inbox())

