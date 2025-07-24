import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY not found in .env or environment.")

# Instantiate the Gemini model explicitly passing the API key
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # "gemini-1.5-pro" also works
    google_api_key=api_key,
    temperature=0.7,
)
# Example usage of the model
response = model.invoke("What is the capital of France?")   
print(response.content)  # Should print "Paris"
