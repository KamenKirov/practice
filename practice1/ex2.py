def find_largest_index(arr):
    largest  = arr[0]
    largest_index = 0
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index =  i
    return largest_index
myarr = [1,2,3,5,17,4,35,322,1,3,2421]
print(find_largest_index(myarr))
if myarr.index(myarr[len(myarr)-1]) == find_largest_index(myarr):
    print("The largest item in the list is in the last element of the list.")    
print()
