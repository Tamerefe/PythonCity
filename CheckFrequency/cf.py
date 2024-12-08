def checkfrequency(fr):
    if 20 < fr <= 20000:
        return "Audio Frequency"
    elif 30000 <= fr <= 300000000:
        return "Radio Frequency"
    else:
        return "Not a valid frequency"

try:
    fr = float(input("Enter the frequency: "))
    print(checkfrequency(fr))
except ValueError:
    print("Please enter a valid number")