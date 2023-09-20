from fivesim import FiveSim, Country, Operator, FiveSimError, ActivationProduct


# load env
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    client = FiveSim(api_key=os.getenv("TOKEN"))
    try:
        result = client.user.buy_number(
            country=Country.POLAND,
            operator=Operator.ANY_OPERATOR,
            product=ActivationProduct.WOLT,
        )

        print(result)
        # code = result.sms[0].activation_code
        # print(code)
    except FiveSimError as e:
        print(e)