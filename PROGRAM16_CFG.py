# Q16. Context-Free Grammar Parsing

# ==============================
# PART 1: CFG Parsing using NLTK
# ==============================

import nltk

# Define grammar rules
# S  = Sentence
# NP = Noun Phrase
# VP = Verb Phrase
# DET = Determiner
# ADJ = Adjective
# N = Noun
# V = Verb

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> DET N | DET ADJ N | N
VP -> V NP | V
DET -> 'the' | 'a'
ADJ -> 'big' | 'small'
N -> 'dog' | 'cat' | 'mat'
V -> 'sat' | 'chased' | 'saw'
""")

# Create parser using grammar
parser = nltk.ChartParser(grammar)

# Test sentences
sentences = [
    "the dog sat",
    "a big cat chased the dog",
    "dog the sat"
]

print("=== NLTK CFG Parser ===")

for sentence in sentences:

    # Split sentence into words
    words = sentence.split()

    # Parse sentence
    trees = list(parser.parse(words))

    # If parse tree is created, sentence is valid
    if len(trees) > 0:
        print(sentence, "-> VALID")
        trees[0].pretty_print()

    # If no parse tree, sentence is invalid
    else:
        print(sentence, "-> INVALID")


# ==================================
# PART 2: Manual CFG Parser
# ==================================

# Store valid words for each grammar category
DET = ["the", "a"]
ADJ = ["big", "small"]
NOUN = ["dog", "cat", "mat"]
VERB = ["sat", "chased", "saw"]


# This function checks whether a word belongs to a category
def match(words, position, word_list):

    # Check that position is inside the sentence
    if position < len(words):

        # Check if current word is in the given list
        if words[position] in word_list:

            # If matched, move to next position
            return position + 1

    # If not matched, return -1
    return -1


# This function checks Noun Phrase
# NP -> DET N
# NP -> DET ADJ N
# NP -> N
def parse_NP(words, position):

    # Rule 1: NP -> DET ADJ N
    p1 = match(words, position, DET)

    if p1 != -1:
        p2 = match(words, p1, ADJ)

        if p2 != -1:
            p3 = match(words, p2, NOUN)

            if p3 != -1:
                return p3

    # Rule 2: NP -> DET N
    p1 = match(words, position, DET)

    if p1 != -1:
        p2 = match(words, p1, NOUN)

        if p2 != -1:
            return p2

    # Rule 3: NP -> N
    p1 = match(words, position, NOUN)

    if p1 != -1:
        return p1

    # If no NP rule matches
    return -1


# This function checks Verb Phrase
# VP -> V NP
# VP -> V
def parse_VP(words, position):

    # First match verb
    p1 = match(words, position, VERB)

    if p1 == -1:
        return -1

    # Rule 1: VP -> V NP
    p2 = parse_NP(words, p1)

    if p2 != -1:
        return p2

    # Rule 2: VP -> V
    return p1


# This function checks full sentence
# S -> NP VP
def parse_sentence(sentence):

    words = sentence.split()

    # First parse NP
    position = parse_NP(words, 0)

    if position == -1:
        return False

    # Then parse VP
    position = parse_VP(words, position)

    if position == -1:
        return False

    # Sentence is valid only if all words are used
    if position == len(words):
        return True
    else:
        return False


print("\n=== Manual CFG Parser ===")

for sentence in sentences:

    if parse_sentence(sentence):
        print(sentence, "-> VALID")
    else:
        print(sentence, "-> INVALID")