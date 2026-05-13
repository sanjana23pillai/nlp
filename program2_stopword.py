file=open("input.txt",'r')
text=file.read()
file.close()
stopwords=["is","a","am","are","the","and"]
words=text.split()
clean_words=[]
for word in words:
    if word.lower() not in stopwords:
        clean_words.append(word)
ans=" ".join(clean_words)
print(ans);
