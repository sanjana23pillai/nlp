ambiguous_words = {
    "bank", "bat", "bark", "light", "match", "right",
    "saw", "duck", "watch", "rock", "spring"
}

syntactic_patterns = [
    "with",
    "flying planes",
    "old men and women"
]
def detect_ambiguity(sentence):
    sentence_lower=sentence.lower()
    words=sentence.split()
    for pattern in syntactic_patterns:
        if pattern in sentence_lower:
            return "Synctactic Ambiguity","Sentence structure can have more than one meaning"
        for word in words:
            word=word.strip(",.!?")
            if word in ambiguous_words:
                return "Semantic Ambiguity","Word has more than one meaning: " 
    return "No ambiguity","No rule matched"

test_sentences = [
    "I saw the man with the telescope",
    "The bank was steep",
    "Flying planes can be dangerous",
    "He saw her duck",
    "I watched the match"
]
for s in test_sentences:
    ambi_type,reason=detect_ambiguity(s)

    print("Sentence:", s)
    print("Type:", ambi_type)
    print("Reason:", reason)