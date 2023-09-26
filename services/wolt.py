from service import perform_instructions, driver, Instruction

def register(
        email: str,
):
    """
    Registers a new account on Wolt using the provided email.

    Args:
        email: The email address to register with.

    Returns:
        bool: True if the registration is successful, False otherwise.

    Example:
        ```python
        email = "test@example.com"
        register(email)
        ```
    """

    register_instructions = [
        # accept cookies
        Instruction('/html/body/div[5]/div/div/div/button[2]/div[3]', 'click'),

        # click login button
        Instruction('/html/body/div[2]/div[2]/div/header/div[2]/div[3]/div/div/button', 'click'),

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
    url: str,
    country: str = None,
    first_name: str = None,
    last_name: str = None,
    country_code: str = None,
    phone_number: str = None,
    referral_code: str = None
):
    """
    Performs the login process on the specified URL with the provided login instructions.

    Args:
        * url: The URL to perform the login process on.
        * country: The country to select in the country selector.
        * first_name: The first name to input.
        * last_name: The last name to input.
        * country_code: The country code to select in the country code selector.
        * phone_number: The phone number to input.
        * referral_code: The referral code to input.

    Returns:
        perform_instructions: The perform_instructions function.

    Example:
        ```python
        url = "https://example.com"
        login(
            url=url,
            country="US",
            first_name="John",
            last_name="Doe",
            country_code="+1",
            phone_number="1234567890",
            referral_code="REF123"
        )
        ```
    """
    
    login_instructions = [

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
        base_url=url,
        instructions=login_instructions,
    )

# result = register('twoja.mama@mymailbox.xxl.st')
# print(f"Registration {'succeeded' if result else 'failed'}")