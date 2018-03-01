a=int(input("enter the range: "))
b=int(input("enter the range: "))
for num in range(a,b):
  sum=0
  temp=num
  while temp>0:
    digi=temp%10
    sum += digi ** 3
    temp //=10
  if num == sum:
    print(num)
    
  
