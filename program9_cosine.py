import math
vector1=[1,2,3]
vector2=[4,5,6]
dot_prod=0
mag1=0
mag2=0
for i in range(len(vector1)):
    dot_prod=dot_prod+vector1[i]*vector2[i]
    mag1=mag1+vector1[i]**2
    mag2=mag2+vector2[i]**2
mag1=math.sqrt(mag1)
mag2=math.sqrt(mag2)
cosine_similarity=dot_prod/(mag1*mag2)
print("Cosine similarity:",cosine_similarity)