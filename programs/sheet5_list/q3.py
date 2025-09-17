# MAX

arr=list(map(int,input().split()))
N=len(arr)
ans=-float("inf")
for i in arr:
    if(i>ans):
        ans=i
print(ans)

# MIN

arr=list(map(int,input().split()))
N=len(arr)
ans=arr[0]
for i in arr:
    if(i<ans):
        ans=i
print(ans)


