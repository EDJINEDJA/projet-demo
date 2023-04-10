from dotenv import load_dotenv
import os

load_dotenv("./env/.env")

API_KEY = os.getenv("API_KEY")
INPUT_DIM =  4
OUTPUT_DIM = 3
LEARNING_RATE = 10e-3
EPOCHS = 10