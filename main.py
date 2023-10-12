import random
arr = [i for i in range(0, 100) if i % 2 == 0]

# implementing binary search

start = 0
end = len(arr)
mid = len(arr)/2
target = int(input("Enter the target element : "))

for i in range(len(arr)):
    mid = (start+end)//2
    if(arr[i]==target):
        print(f"The elements found at index {i}")
        break
    if(mid>target):
        end = mid-1
    if(mid<target):
        start = mid+1
    else:
        print("Element not found")
