file=open("input.txt","r")
text=file.read()
file.close()
stopwords=["is","the","and","a"]
words=text.split()
cleaned_text=[]
for word in words:
    word=word.lower()
    if word not in stopwords:
        cleaned_text.append(word)
ans=" ".join(cleaned_text)
print(ans)