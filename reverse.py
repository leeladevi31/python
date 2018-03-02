a=int(input("Enter the number: "))
rev=0
while(a>0):
    x=a%10
    rev=rev*10+x
    a=a//10
print("Reverse of the number:",rev)
