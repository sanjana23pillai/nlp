import re
file=open("input.txt",'r')
text=file.read()
file.close()
sentences=re.split("r[.!?]",text)
total_tokens=0
for sentence in sentences:
    sentence=sentence.strip()
    if sentence!=" ":
        print("Sentence:",sentence)
        words=sentence.split()
        print("Words:",words)
        total_tokens=total_tokens+len(words)
print("Total tokens:",total_tokens)
