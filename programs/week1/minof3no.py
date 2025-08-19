A=int(input("Enter first number : "))
B=int(input("Enter second number : "))
C=int(input("Enter third number : "))
if(A<B and A<C):
    print("A is smallest ")
elif(B<C and B<A):
    print("B is smallest ")
else:
    print("C is smallest ")