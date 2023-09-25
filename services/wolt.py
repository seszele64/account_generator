from service.instructions import Instruction, perform_instructions, driver

def register(
        email: str,
):
    register_instructions = [
        # accept cookies
        Instruction(
            '/html/body/div[5]/div/div/div/button[2]/div[3]', 'click'
        ),

        # click login button
        Instruction(
        '/html/body/div[2]/div[2]/div/header/div[2]/div[3]/div/div/button', 'click'),

        # input email
        Instruction('//*[@id="method-select-email"]', 'input', email),

        # click next button
        Instruction('/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/button/div[3]', 'click'),

        # wait for the confirmation modal to load -> proves that email has been sent
        Instruction('/html/body/div[7]/div/aside/div[4]/div/div[1]/div/div/button/div[3]', 'wait'),
    ]


    return perform_instructions(
        driver=driver,
        base_url='https://wolt.com/en',
        instructions=register_instructions
    )

def login(
    country: str = None,
    first_name: str = None,
    last_name: str = None,
    country_code: str = None,
    phone_number: str = None,
    referral_code: str = None
):
    
    Instructions = [

        # country selector
        Instruction('/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[2]/label/select', 'select', country),

        # ----------------------------------- Name ----------------------------------- #

        # first name
        Instruction('//*[@id="create-account-first-name"]', 'input', first_name),
        # last name
        Instruction('//*[@id="create-account-last-name"]', 'input', last_name),

        # ----------------------------------- phone ---------------------------------- #

        # country code
        Instruction('/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[4]/div[1]/label/select', 'select', country_code),
        # phone number
        Instruction('//*[@id="create-account-phone-number"]', 'input', phone_number),

        # ----------------------------------- referral ---------------------------------- #

        # referral code
        Instruction('//*[@id="create-account-referral-code"]', 'input', referral_code),
    ]

    return perform_instructions(
        driver=driver,
        base_url='https://wolt.com/en',
        instructions=Instructions
    )

# result = register('twoja.mama@mymailbox.xxl.st')
# print(f"Registration {'succeeded' if result else 'failed'}")