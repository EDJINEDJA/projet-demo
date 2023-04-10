from dotenv import load_dotenv
import os

load_dotenv("./env/.env")

API_KEY = os.getenv("API_KEY")
NBR_ITER =  5