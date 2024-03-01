import pandas as pd
from sentence_transformers import SentenceTransformer
import json
import numpy as np

# Load the CSV file
df = pd.read_csv("CompleteMainText.csv", index_col=0)  # Replace "your_file.csv" with the path to your CSV file


# Check if the 'Vector' column exists, and if so, drop it
if 'Vector' in df.columns:
    df = df.drop(columns=['Vector'])
if 'DocID' in df.columns:
    df = df.drop(columns=['DocID'])
if 'Embeddings' in df.columns:
    df = df.drop(columns=['Embeddings'])

    
# Initialize the model
model = SentenceTransformer("NeuML/pubmedbert-base-embeddings")

# Function to generate embeddings
def generate_embeddings(text):
    embeddings = model.encode(text)
    return embeddings.tolist()  # Convert numpy array to list for JSON serialization

# Apply the function to generate embeddings for each row in the Text column
df['Vector'] = df['Text'].apply(generate_embeddings)

# Convert the DataFrame to a JSON format
json_data = df.to_json(orient="records")

# Save the JSON data to a file
with open("output_file.json", "w") as file:  # Replace "output_file.json" with your desired output file name
    file.write(json_data)

print("Conversion to JSON completed with embeddings.")
