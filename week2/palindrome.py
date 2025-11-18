A=int(input("Enter a number : "))
ori_num=A
rev=0
while(A>0):
    rev=rev*10+A%10
    A=A//10
if(rev==ori_num):
    print("YES given number is palindrome ")
else:
    print("Not palindrome ")

