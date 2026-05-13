# Q14. BLEU Score Manual - Easy but Proper Version
# This version uses unigram and bigram precision

import math

reference = "the cat sat on the mat"
candidate = "the cat is on the mat"

ref = reference.split()
cand = candidate.split()

# Function to create n-grams
def make_ngrams(words, n):
    ngrams = []

    for i in range(len(words) - n + 1):
        gram = tuple(words[i:i+n])
        ngrams.append(gram)

    return ngrams


# Function to calculate precision
def precision(ref, cand, n):
    ref_ngrams = make_ngrams(ref, n)
    cand_ngrams = make_ngrams(cand, n)

    match = 0

    for gram in cand_ngrams:
        if gram in ref_ngrams:
            match += 1

    return match / len(cand_ngrams)


# 1-gram precision
p1 = precision(ref, cand, 1)

# 2-gram precision
p2 = precision(ref, cand, 2)

# Brevity Penalty
if len(cand) >= len(ref):
    BP = 1
else:
    BP = math.exp(1 - len(ref) / len(cand))

# BLEU using 1-gram and 2-gram
bleu = BP * math.exp((0.5 * math.log(p1)) + (0.5 * math.log(p2)))

print("Reference:", reference)
print("Candidate:", candidate)

print("1-gram precision:", p1)
print("2-gram precision:", p2)
print("Brevity Penalty:", BP)
print("BLEU Score:", bleu)