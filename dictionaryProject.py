import json

data = json.load(open("data.json","r"))
word = input("Please enter a word : ")

def word_check():
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return "Please enter the word correctly."
    

if type(word_check()) == list:
    for x in word_check():
        print(x)
else:
    print(word_check())
