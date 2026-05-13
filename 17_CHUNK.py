# Q17. Chunking - Noun Phrase Identification
# NP rule: DET? ADJ* NOUN

sentence = "The quick brown fox jumped over a lazy sleeping dog"

# Word lists
DET_WORDS = ["the", "a", "an", "this", "that", "these", "those"]
ADJ_WORDS = ["quick", "brown", "lazy", "sleeping"]
NOUN_WORDS = ["fox", "dog", "cat", "mat", "park", "man", "woman"]
VERB_WORDS = ["jumped", "ran", "sat", "chased", "is", "are", "was", "were", "over"]

# Function to assign POS tag
def pos_tag(word):
    word = word.lower()

    if word in DET_WORDS:
        return "DET"

    elif word in ADJ_WORDS:
        return "ADJ"

    elif word in NOUN_WORDS:
        return "NOUN"

    elif word in VERB_WORDS:
        return "VERB"

    elif word.endswith("ly"):
        return "ADV"

    else:
        return "NOUN"


# Split sentence into words
tokens = sentence.split()

# Store word and POS tag together
tagged = []

for word in tokens:
    tag = pos_tag(word)
    tagged.append((word, tag))

print("POS Tags:")
for word, tag in tagged:
    print(word, "->", tag)


# Chunking part
# Rule: NP = optional DET + zero or more ADJ + one NOUN

print("\nNoun Phrases:")

i = 0

while i < len(tagged):

    chunk = []
    j = i

    # Check optional determiner
    if tagged[j][1] == "DET":
        chunk.append(tagged[j][0])
        j = j + 1

    # Check zero or more adjectives
    while j < len(tagged) and tagged[j][1] == "ADJ":
        chunk.append(tagged[j][0])
        j = j + 1

    # Check required noun
    if j < len(tagged) and tagged[j][1] == "NOUN":
        chunk.append(tagged[j][0])
        print("NP:", chunk)
        i = j + 1

    else:
        i = i + 1