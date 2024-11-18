from textblob import TextBlob

def correct(text):
    corrected = str(TextBlob(text).correct())
    return corrected

text = input("Enter a sentence: ")

corrected = correct(text)
print(f"Corrected: {corrected}")
