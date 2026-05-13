prior={
    "positive":0.5,
    "negative":0.5
}
test_sentences=[
    "movie good happy",
    "movie bad boring",
    "movie excellent good"
]
word_probs = {
    "Positive": {
        "movie": 0.2,
        "good": 0.6,
        "happy": 0.5,
        "excellent": 0.7,
        "bad": 0.1,
        "sad": 0.1,
        "boring": 0.1
    },

    "Negative": {
        "movie": 0.2,
        "good": 0.1,
        "happy": 0.2,
        "excellent": 0.1,
        "bad": 0.7,
        "sad": 0.6,
        "boring": 0.5
    }
}
for sentence in test_sentences:
    words=sentence.lower().split()
    scores={}
    for class_name in prior:
        score=prior[class_name]
        for word in words:
            score=score*word_probs[class_name][word]
        scores[class_name]=score
    predicted_class=max(scores,key=scores.get)
    print("Sentence",sentence)
    print("Predicted class")