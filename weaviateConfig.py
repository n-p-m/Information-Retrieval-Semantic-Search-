#Resource Link-> https://weaviate.io/developers/weaviate/starter-guides/custom-vectors


import weaviate
import json

client = weaviate.Client(
    url = "https://my-first-test-4s34zp9m.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.auth.AuthApiKey(api_key="4ik2R6XCHiBSVNTZ0BKd0UnrDhVhaLVWb8JZ"),  # Replace w/ your Weaviate instance API key
)
# Class definition object. Weaviate's autoschema feature will infer properties when importing.
class_obj = {
    "class": "Article",
    "vectorizer": "none",
}

# Add the class to the schema
client.schema.create_class(class_obj)

file_path = 'output_file.json'

# Open the JSON file and load its contents into a variable
with open(file_path, 'r') as file:
    data = json.load(file)

# import requests
# url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny+vectors.json'
# resp = requests.get(url)
# data = json.loads(resp.text)

# Configure a batch process
client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:
    # Batch import all Questions
    for i, d in enumerate(data):
        print(f"importing question: {i+1}")

        properties = {
            "title": d["Title"],
            "text":d["Text"],
            "url": d["URL"],
        }

        batch.add_data_object(properties, "Article", vector=d["Vector"])