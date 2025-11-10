import os
from dotenv import load_dotenv


load_dotenv('.env')


class Config:
    BASE_URL = os.getenv('BASE_URL')
