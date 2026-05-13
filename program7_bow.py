sentences = [
    "I love machine learning",
    "I love deep learning",
    "Deep learning is powerful"
]

vocabulary = ["i", "love", "machine", "learning", "deep", "is", "powerful"]
bow_matrix=[]
for sentence in sentences:
    words=sentence.lower().split()
    row=[]
    for word in vocabulary:
        row.append(words.count(word))
    bow_matrix.append(row)
for row in bow_matrix:
    print(row)