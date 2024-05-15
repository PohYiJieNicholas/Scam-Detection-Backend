from flask import Flask, jsonify
from OpenSSL import SSL
import torch
from torch.utils.data import DataLoader, TensorDataset, RandomSampler
from transformers import GPT2ForSequenceClassification, GPT2Tokenizer, AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

app = Flask (__name__)

def prediction(conversation):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token

    model = GPT2ForSequenceClassification.from_pretrained('my_gpt_model')
    label_map = {0: "Normal Message", 1: "Fraudulent Message"}

    
    # Example of preparing an input for prediction
    texts = [conversation]
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=512, return_tensors="pt")

    # Move tensors to the same device as model
    input_ids = encodings['input_ids']
    attention_mask = encodings['attention_mask']

    # Predict
    model.eval()
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        predictions = torch.argmax(outputs.logits, dim=-1)

    print([label_map[label.item()] for label in predictions])

    return [label_map[label.item()] for label in predictions]

@app.route('/')
def main():
    return 'Hello World'

@app.route('/api/data', methods=['GET'])
def get_data():
    result = prediction("Hello, I'm calling from the survey department. You've been selected to participate in a paid survey. Can you confirm your bank details for the payment?")

    data = {
        "prediction": result[0]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)