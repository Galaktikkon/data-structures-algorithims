def binarysearch(arr, n, k):
    # code here
    left = 0
    right = n-1
    mid = (left+right)//2
    while left <= right:
        if arr[mid] < k:
            left = mid+1
        elif arr[mid] > k:
            right = mid-1
        else:
            return mid
        mid = (left+right)//2
    return -1


arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(binarysearch(arr, 14, 1))
