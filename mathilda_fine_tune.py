import os
import openai
from dotenv import load_dotenv


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.create(training_file="file-XGinujblHPwGLSztz8cPS8XY")
