import json
import difflib
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    word =  word.lower()
    if word in data:
        return data[word]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len (get_close_matches(word, data.keys())) > 0:
        get_close_matches(word, data.keys(),n=6, cutoff=0.4)
        user = input("Did you mean %s? Enter Y for yes and N for No" % get_close_matches(word,data.keys())[0])
        if user == "Y":
            return(data[get_close_matches(word,data.keys())[0]])
        else:
            return("Didn't Understand your entry :)")
    else:
        return("The word doesn't exist.")

word = input("Enter Word:")

meaning = translate(word)

if type(meaning) == list:
    for i in meaning:
    print(i)

else:
    print(meaning)