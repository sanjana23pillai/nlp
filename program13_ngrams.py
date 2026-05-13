import random
corpus="cat mat the hello the cat bat mat the bat hello ball"
words=corpus.split()
bigram={}
for i in range(len(words)-1):
    current=words[i]
    next=words[i+1]
    if current not in bigram:
        bigram[current]=[]
    bigram[current].append(next)
for word in bigram:
    print(word,"->",bigram[word])
curr="the"
generated=[curr]
for i in range(20):
    if curr in bigram:
        next_word=random.choice(bigram[curr])
        generated.append(next_word)
        curr=next_word
    else:
        break
print(" ".join(generated))
        