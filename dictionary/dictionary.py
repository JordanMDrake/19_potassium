import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def define(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        # todo -- fix input for 'Yes' and 'No' options - program doesn't currently allow for
        #       both upper and lowercase input
        yn = input("Did you mean %s instead? Enter Y if 'yes' or N if 'no'" % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "Sorry, that word doesn't exist. Please double-check your spelling."
        else:
            return "Sorry, I didn't understand your entry"
    else:
        return "Sorry, that word doesn't exist. Please double-check your spelling."


word = input("Enter a word: ")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)

# todo -- allow for program to accept proper nouns (Idaho, Lincoln, etc.) - check against capitalized first letter
# todo -- institute a while loop so program runs continuously until it is explicity stopped by user
# todo -- allow for inclusion of acronyms (USA, NATO, etc.)
