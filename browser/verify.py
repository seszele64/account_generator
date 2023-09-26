
import requests
import time
import random

# Verify link
class LinkVerifier:
    def __init__(self, headers: dict = None):
        # self.link = link
        self.headers = headers
        self.retry = 0

    # visit link with given headers
    def visit(self, link: str) -> bool:
        try:
            response = requests.get(link, headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        
    # verification status
    def verification_loop(self, max_retries: int = 1):

        # visit link
        if self.visit():
            print('Verification successful')
            return True
        else:
            print('Verification failed')
            if self.retry < max_retries:
                self.retry += 1
                print(f'Retrying verification... ({self.retry}/{max_retries})')
                time.sleep(random.uniform(1, 3))
                self.verification_loop(self.retry, max_retries)
            else:
                print('Max retries reached')
                raise Exception('Max retries reached')
            
    



            


        


            
        
        

    