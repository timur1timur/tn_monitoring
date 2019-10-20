from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os
import requests


key_var_name = 'TEXT_ANALYTICS_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

endpoint_var_name = 'TEXT_ANALYTICS_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

credentials = CognitiveServicesCredentials(subscription_key)

sentiment_url =     "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment"
keyword_url =       "https://westcentralus.api.cognitive.microsoft.com//text/analytics/v2.1/keyphrases"

def sentens(text):
    documents = {"documents": [
        {"id": "1", "language": "ru",
            "text": text}
    ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentiments = response.json()
    return sentiments

def keyword(text):
    documents = {"documents": [
        {"id": "1", "language": "ru",
         "text": text}
    ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(keyword_url, headers=headers, json=documents)
    key_phrases = response.json()
    return key_phrases
