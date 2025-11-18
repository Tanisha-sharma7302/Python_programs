# input aeiOUz
# output ###z###z
# small vowel letter="#"
#capital vowel=delete
# consonent as it is print



#  A="aeiOUz"
#  Output:
#  "###z###z



A=input(" enter string")
vowels="aeiou"
ans=''
A=A+A
for i in range(len(A)):
    if(A[i].isupper()):
        continue
    else:
        if(A[i] in vowels):
            ans+='#'
        else:
            ans+=A[i]
print(ans)




