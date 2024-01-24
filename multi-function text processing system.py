#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:30:01 2024

@author: derinberktay
"""

import requests
import json

#PLEASE REPLACE WITH YOUR OWN API KEY
COHERE_API_KEY = 'YOUR_API_KEY'
COHERE_API_URL = 'https://api.cohere.ai'

headers = {
    'Authorization': f'Bearer {COHERE_API_KEY}',
    'Content-Type': 'application/json',
}

def generate_text(prompt):
    data = {
        "prompt": prompt,
        "max_tokens": 50, # You can also adjust this based on your need
        "temperature": 0.5
    }
    response = requests.post(f'{COHERE_API_URL}/generate', headers=headers, json=data)
    return response.json()['text']

def analyze_sentiment(text):
    data = {
        "inputs": text,
        "model": "large",
        "task": "sentiment-analysis"
    }
    response = requests.post(f'{COHERE_API_URL}/classify', headers=headers, json=data)
    return response.json()['classifications']

def classify_text(text, categories):
    data = {
        "inputs": text,
        "model": "large",
        "task": "classification",
        "categories": categories
    }
    response = requests.post(f'{COHERE_API_URL}/classify', headers=headers, json=data)
    return response.json()['classifications']

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate Text")
        print("2. Analyze Sentiment")
        print("3. Classify Text")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            prompt = input("Enter a prompt for text generation: ")
            generated_text = generate_text(prompt)
            print(f"Generated Text: {generated_text}")

        elif choice == '2':
            text = input("Enter text for sentiment analysis: ")
            sentiment = analyze_sentiment(text)
            print(f"Sentiment: {sentiment}")

        elif choice == '3':
            text = input("Enter text for classification: ")
            categories = input("Enter categories separated by comma: ").split(',')
            classification = classify_text(text, categories)
            print(f"Classification: {classification}")

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
