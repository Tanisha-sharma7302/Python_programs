T=int(input())
result=[]
for i in range(T):
    s=input()
    rev=s[::-1]
    if(rev==s):
        result.append(1)
    else:
        result.append(0)
for j in range(T):
    print(result[j])

    

T=int(input())
reverse=[]
for i in range(T):
    s=input()
    rev=reversed(s)
    p=("".join(rev))
    if(s==p):
        reverse.append(1)
    else:
        reverse.append(0)

for j in range(T):
    print(reverse[j])