def printRepeating(arr, size):
 
    print("Repeating elements are ",
                         end = '')
    for i in range (0, size):
        for j in range (i + 1, size):
            if arr[i] == arr[j]:
                print(arr[i], end = ' ')
     
arr = [1,4,26,4,2,8,5,1,6,3,4,7,5,9]
arr_size = len(arr)
printRepeating(arr, arr_size)
