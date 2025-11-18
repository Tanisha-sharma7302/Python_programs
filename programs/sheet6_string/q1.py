N=int(input())
result1=[]
result2=[]
vowels="aeiouAEIOU"

for i in range(N):
    s=input()
    vowel=0
    consonant=0
    for j in s:
        if j in vowels:
            vowel+=1
        else:
            consonant+=1
    result1.append(vowel)
    result2.append(consonant)
for k in range(N):
    print(result1[k],result2[k])
            
    



