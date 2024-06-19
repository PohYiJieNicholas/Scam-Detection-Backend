import torch
import pandas as pd
import numpy as np
import time
import json

from flask import Flask, jsonify, request
from torch.utils.data import DataLoader, TensorDataset, RandomSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification, GPT2ForSequenceClassification, GPT2Tokenizer


app = Flask (__name__)

def load_model():
    global tokenizer
    global model

    tokenizer = GPT2Tokenizer.from_pretrained('./models/tuned_gpt_model')
    model = GPT2ForSequenceClassification.from_pretrained('./models/tuned_gpt_model')

def prediction(input):
 
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    start_time = time.time()
    
    # Tokenize the input data
    inputs = tokenizer(input, return_tensors='pt', padding=True, truncation=True)

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted class
    predictions = torch.argmax(outputs.logits, dim=-1)
    # Map the predictions to 'normal' or 'fraud'
    label_map = {1: 'normal', 0: 'fraud'}
    predicted_labels = [label_map[pred.item()] for pred in predictions]

    end_time = time.time()
    time_taken = end_time - start_time

    return predicted_labels[0], time_taken


with app.app_context():
    load_model()

@app.route('/')
def main():
    return 'Hello World'

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    print("Content: ", data)

    if 'input' not in data:
        return 'Error: No message provided'
    else:
        input = data['input']
        print("Input: ", input)
        output, predict_timing = prediction(str(input))

    data = {
        "message": "Success",
        "output": output,
        "timeTaken": str(predict_timing)
    }

    return jsonify(data)

# @app.route('/api/load_model', methods=['GET'])
# def load_model():

#     model, tokenizer = load_model()
#     return model, tokenizer


if __name__ == '__main__':
    app.run(host='192.168.68.52',port = '8080', debug=True)