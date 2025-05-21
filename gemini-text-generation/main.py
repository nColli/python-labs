# Chat con Gemini sin contexto y sin almacenar respuestas anteriores
from google import genai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_client():
    key = os.getenv('gemini_api_key')
    client = genai.Client(api_key=key)
    return client

def get_response(client, query):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=query
    )

    return response.text


def main():
    configure()
    client = get_client()

    query = input("User: ")

    while (query.lower() != "callate"):
        response = get_response(client, query)
        print("Gemini:", response)
        query = input("User: ")

main()