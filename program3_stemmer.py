file=open("input.txt",'r')
text=file.read()
file.close()
words=text.split()
stemmed_words=[]
for word in words:
    word=word.lower()
    if word.endswith("ing"):
        word=word[:-3]
    elif word.endswith("ed"):
        word=word[:-2]
    elif word.endswith("s"):
        word=word[:-1]
    stemmed_words.append(word)
ans=" ".join(stemmed_words)
print(ans)