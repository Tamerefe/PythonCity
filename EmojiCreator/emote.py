import emoji

def textToEmote(text):
    return emoji.emojize(text)

print("1. Enter text with emoji codes (e.g., 'I love :pizza:')")
print("2. Use ':' to wrap emoji codes")
inpuText = input("Enter text: ")

print(textToEmote(inpuText))