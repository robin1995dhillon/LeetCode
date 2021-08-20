#Time O(N)
#Space O(1)
def validMountainArray(arr):
    if(len(arr)<3):
        return False
    i = 1
    while(i<len(arr) and arr[i]>arr[i-1]):
        i = i+1
    if(i == 1 or i == len(arr)):
        return False
    while(i<len(arr) and arr[i]<arr[i-1]):
        i = i+1

    print(i == len(arr))


arr = [0,2,3,4,5,1,1]

validMountainArray(arr)