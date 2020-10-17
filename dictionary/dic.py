import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.3)) > 0:
        closeWord = get_close_matches(word, data.keys(), cutoff = 0.3)[0]
        print(f"Did you mean {closeWord} instead of {word}")
        decide = input("Press y for Yes or n for No: ")
        if decide == "y":
            return data[closeWord]
    else:
        return "Not Found!"


def formatOutput(output):
    if type(output) == list:
        for item in output:
            print(f"Possible meaning: {item}")
    else:
        print(output)


word = input("Search for word: ")
output = translate(word)
print(formatOutput(output))

# print(get_close_matches("abc", ["abcd", "abcde", "cba"], cutoff = 0.3))
