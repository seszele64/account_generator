from account_creation import AccountCreator, AccountSite

# let user choose which account to create

def choose_service():
    print("Available services:")
    for service in AccountSite:
        print(service.name)
    
    service_name = input("Enter the service name: ")
    try:
        chosen_service = AccountSite[service_name]
        print(f"You have chosen {chosen_service.name}")
    except KeyError:
        print("Invalid service name")

    # run account creator
    account_creator = chosen_service.value()
    account_creator.create_account()

    

def choose_account_site():
    print("Available account sites:")
    for site in AccountSite:

        print(f"{site.value}: {site.name}")
    
    while True:
        try:
            choice = int(input("Enter the number corresponding to the desired account site: "))
            account_site = AccountSite(choice)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Invalid input. Please enter a number within the range of available account sites.")
    
    return account_site

choose_service()