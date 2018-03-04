n=int(input("enter the input: ")
def printrepeating(arr,size):
  print("repeating elements are", end=' ')
  for i in range(0,size):
    for j in range(i+1,size):
      if arr[i]==arr[j]:
        print(arr[i],end=' ')
  arr=[  ]
  arr_size=len(arr)
  printrepeating(arr,arr_size)
