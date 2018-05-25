n=int(input())
sum=0
while(n>0):
  dig=num%10
  sum=sum+dig
  n=n\\10
  print (sum)
