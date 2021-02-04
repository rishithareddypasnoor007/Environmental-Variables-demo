import os
from dotenv import load_dotenv
load_dotenv()
if __name__ == '__main__':
    secret=os.getenv("SECRET_KEY")
    print(secret)

