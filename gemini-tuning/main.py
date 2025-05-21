# Chat con Gemini sin contexto y sin almacenar respuestas anteriores
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_client():
    key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=key)
    return client

def get_response(client, query):
    response = client.models.generate_content(
        model="gemini-1.5-flash-001", 
        config=types.GenerateContentConfig(
            system_instruction="la conversación sera solo en español"),
        contents=query
    )

    return response.text

def get_models(client):
    for model_info in client.models.list():
        print(model_info.name)

def get_tuning_example(client):
    model = 'models/gemini-1.5-flash-001-tuning'
    training_dataset = types.TuningDataset(
        examples=[
            types.TuningExample(
                text_input=f'Input text {i}',
                output=f'Output text {i}',
            )
            for i in range(5)
        ],
    )
    tuning_job = client.tunings.tune(
        base_model=model,
        training_dataset=training_dataset,
        config=types.CreateTuningJobConfig(
            epoch_count=1, tuned_model_display_name='test_dataset_examples model'
        ),
    )
    print(tuning_job)
    return tuning_job

def main():
    configure()
    client = get_client()

    #tuning_job = get_tuning_example(client)
    tuning_job = client.tunings.get(name="tunedModels/testdatasetexamples-model-phipckz6aflulm")
    #print(tuning_job)

    response = client.models.generate_content(
        model=tuning_job.tuned_model.endpoint,
        contents='why is the sky blue?',
    )

    print(response.text)

    #tuned_model = client.models.get(model=tuning_job.tuned_model.model)
    #print(tuned_model)

    #for model in client.models.list(config={'page_size': 10, 'query_base': False}):
    #    print(model)

main()