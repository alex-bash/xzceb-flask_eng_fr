""" translation module """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

"""apikey = os.environ['apikey']"""
"""url = os.environ['url']"""

authenticator = IAMAuthenticator('kcbRWpjDszNmqhTc1aFJyUWmijQJdHCRwsieRdcxDvo_')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6713f952-4f9b-47c6-9e3a-4a976dd825a6')

# translates english text to french
def english_to_french(english_text):
    """ check for empty input """
    if not english_text:
        return ''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

# translates french text to english
def french_to_english(french_text):
    """ check for empty input """
    if not french_text:
        return ''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
