file=open("input.txt",'r')
text=file.read()
file.close()
words=text.split()
for word in words:
    word=word.strip(",.!?").lower()
    if word.endswith("ly"):
        tag="Adverb"
    elif word.endswith("ing"):
        tag="Verb"
    elif word.endswith("ed"):
        tag="Verb"
    elif word in ["the","a","an"]:
        tag="Determiner"
    elif word in ["me","you","he","she"]:
        tag="Pronoun"
    else:
        tag="Noun"
    print(word,": ",tag)
