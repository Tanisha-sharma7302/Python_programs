N=int(input("Enter a number : "))
for i in range(2,N/2):
     if(N>1):
         if(N%i==0):
             print("not prime ")
             break
         else:
             print("prime ")
         else:
     print("not prime ")
     