#l1=[1,2,3,4,5,6]
# print(l1)
# print(len(l1))
# print(l1[-1])
# l2=["mohan", 5.0, 5, "true"]

# print(l2)
#sum=0
 #for i in range(len(l1)):
  #  sum=l1[i]+sum
 #print(sum)
 

# l1=[1,2,3,4,5,6]
#l1.append(100)
#print(l1)
#l1.insert(5,80)
#print(l1)
#l1.insert(100,1990)
#print(l1)
#l1.extend([8,'Tanisha',61,True])
#print(l1)
#l1.pop()
#print(l1)
#l1.remove(1990)
#print(l1)
#l1.reverse()
#print(l1)
#l1.__reversed__()
#print(l1)
# l1[::-1]
# print(l1)
# l1=[1,2,3,4,5,6]
# n=len(l1)
# for i in range(0,n//2):
#     l1[i],l1[n-1-i]=l1[n-1-i],l1[i]
# print(l1)

# a="hello how are you"
# print(a.split())


# a="hello-how-are-you"
# print(a.split("-"))


# num="1 2 3 4"
# print(num.split())


# a=list(map(int,input().split()))
# print(a)


# a=map(int,input().split())
# print(a)


#given an array compute the sum of all array.
# arr=list(map(int,input().split()))
# ans=0
# for i in range(len(arr)):
#     ans=ans+arr[i]
# print(ans)


#given an array find the max value in it.
# arr=list(map(int,input().split()))
# ans=-float("inf")
# for i in arr:
#     if(ans<i):
#         ans=i
# print(ans)


# ans=-float("inf")

# given an array and a target number. find number of occurance of target number in the array.
 
# arr=list(map(int(input().split()))
# target=int(input())
# count=0
# for i in range(len(arr)):
#     if(arr[i]==target):
#         count+=1
# print(count)

# given an array and an increment number generate a new array which contains all values of original array increased by increment value.

# arr=list(map(int,input().split()))
# inc=int(input())
# new_arr=[]

# for i in arr:
#     new_arr.append(i+inc)
# print(new_arr)

# square question
# arr=list(map(int,input().split()))
# inc=int(input())
# square=inc*inc
# new_arr=[]

# for i in arr:
#     new_arr.append(i+square)
# print(new_arr)

# filter out the odd numbers

# arr=list(map(int,input().split()))
# oddNum_arr=[]

# for i in arr:
#     if(i%2!=0):
#         oddNum_arr.append(i)
# print(oddNum_arr)

   
# arr=list(map(int(input().split())))
# target=int(input())
# for i in arr:
#     if (target==arr[i]):
#         print(i)
    


list1=[1, 2, 3, 4, 4, 5]
list2=[5, 6, 7, 8]
result=[]
for i in range(len(list2)):
    result.append(list1[i] + list2[i])
print(result)

 







