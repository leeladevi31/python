x = int(input("enter the number: "))
if x>1:
  for i in range(2, x):
    if(x%i)==0:
      print("not a prime")
      break
    else:
      print("it is prime")
else:
  print("no")
    
