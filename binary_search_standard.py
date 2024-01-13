# Binary search is subtle, a minor change can lead to incorrect behavior. 
# Some possible confusing points:
# 1.right = len(arr) VS right = len(arr)-1
# 2.right = mid VS right = mid-1
# 3.left < right VS left == right
# 4.if arr[mid] == target: return mid VS right = mid


def binary_search_standard(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



arr =[1, 3 ,5,7 ,9]
target = 4
print(f"binary_search_standard on {target}, returns {binary_search_standard(arr, target)}")
