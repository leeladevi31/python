a=int(input("enter the value: "))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
 if(temp==rev):
    print("it is a palindrom")
 else:
 print("it is not a palindrom")
