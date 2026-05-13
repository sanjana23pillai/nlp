document=input("Enter a document: ")
words=document.lower().split()
total_Words=len(words)
tf={}
for word in words:
    word=word.strip(".,!?")
    if word in tf:
        tf[word]=tf[word]+1
    else:
        tf[word]=1
for word in tf:
    term_freq=tf[word]/total_Words
    print(word,tf[word],term_freq)