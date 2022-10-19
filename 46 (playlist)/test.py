import secrets
from dotenv import load_dotenv
load_dotenv()


import os
test = os.environ.get("SECRET")
print(test)