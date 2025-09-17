arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr=[]
for i in range(len(arr1)):
    arr.append(arr1[i]+arr2[i])
print(arr)

