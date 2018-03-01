num=int(input("enter the input: "))
sum=0
temp=num
while temp>0:
digi = temp%10
sum += digi ** 3
temp //=10
if num == sum:
  print("it is an armstrong number")
else:
  print("it is not an armstrong number")
