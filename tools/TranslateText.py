from googletrans import Translator

def translating(str):
    translator = Translator()
    return translator.translate(str, dest='en')