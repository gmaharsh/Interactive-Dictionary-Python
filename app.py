import json

data = json.load(open("data.json"))

def translate(word):
    word =  word.lower()
    if word in data:
        return data[word]
    else:
        return("The word doesn't exist.")

word = input("Enter Word:")

print(translate(word))