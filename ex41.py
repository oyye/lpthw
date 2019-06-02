import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
 "class %%%(%%%):":
 "Make a class named %%% that is-a %%%.",
 "class %%%(object):\n\tdef __init__(self, ***)" :
 "class %%% has-a __init__ that takes self and *** params.",
 "class %%%(object):\n\tdef ***(self, @@@)":
 "class %%% has-a function *** that takes self and @@@ params.",
 "*** = %%%()":
 "Set *** to an instance of class %%%.",
 "***.***(@@@)":
 "From *** get the *** function, call it with params self, @@@.",
 "***.*** = '***'":
 "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word, encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_name = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        count = random.randint(1, 3)
        param_names.append(", ".join(random.sample(WORDS, count)))

    for result in snippet, phrase:
        #result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)
        for w in other_name:
            result = result.replace("***", w, 1)
        for w in param_names:
            result = result.replace("@@@", w, 1)
        
        results.append(result)

    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)
            input("> ")
            print(f"ANSWER: {answer}")
except EOFError:
    print("\nBye")

