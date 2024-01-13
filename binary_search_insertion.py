# Binary search is subtle, a minor change can lead to incorrect behavior. 
# Some common confusing points:

# 1.right = mid VS right = mid-1
# 2.right = len(arr) VS right = len(arr)-1
# 3.while left < right VS while left <= right
# 4.if arr[mid] == target: return mid VS right = mid


# This is the correct impl of binary search FOR FINDING INSERTION POINT
# If target exists, return the index of the target in arr
# If not, return the index where the target could be inserted while maintaining the sorted order of the array.
def binary_search_insertion_correct(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid +1
        else:
            right = mid
    return left


# Bug 1: setting right = mid-1
# When we want to find the insertion point, we need to include 
# mid point into the new area, because that might be the insertion point
def binary_search_insertion_buggy1(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid +1
        else:
            # right = mid
            right = mid-1
    return left


# Bug 2: setting right = len(arr) - 1
# When we want to find the insertion point, if all elements are smaller than target,
# we need to return len(arr), which exceeds the last index of original arr
def binary_search_insertion_buggy2(arr, target):
    # left, right = 0, len(arr)
    left, right = 0, len(arr) - 1 
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid +1
        else:
            right = mid
    return left

# Bug 3: setting to while left <= right:
# Since we set right = mid, if we further allow left == right, then it
# will cause infinity loop
def binary_search_insertion_buggy3(arr, target):
    looped_time = 0

    left, right = 0, len(arr)
    # while left < right:
    while left <= right:
        looped_time+=1
        if looped_time >= 1000:
            print(f"binary_search_insertion_buggy3 has run loop 1k times!")
            return -1

        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid +1
        else:
            right = mid
    return left


# Bug 4: Add if arr[mid] == target: return mid 
# This would return the index as soon as a value in arr equal to target is found,
# meaning if there are multiple values equal to target, a random one of them will be returned. 
# This can be potentially problematic, because in some cases we have duplciates in arr
# and we want to actually find the first occurence, rather than a random one in the consecutive
# sequece of duplicates, for example Leetcode 1235
def binary_search_insertion_maybebuggy(arr, target):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid +1
        elif arr[mid] == target:
            return mid
        else:
            right = mid
    return left


arr =[1,3,5,5,7,9]

print(f"\n")
print(f"First buggy implementation sets right = mid-1")
target = 2 # Correct impl should return 1 (inserted after 1)
print(f"Running binary_search_insertion_correct on {target}, returns {binary_search_insertion_correct(arr, target)}")
print(f"Running binary_search_insertion_buggy1 on {target}, returns {binary_search_insertion_buggy1(arr, target)}")
print(f"\n")

print(f"Second buggy implementation sets right = len(arr) - 1")
target = 10 # Correct impl should return 7 (inserted after 9)
print(f"Running binary_search_insertion_correct on {target}, returns {binary_search_insertion_correct(arr, target)}")
print(f"Running binary_search_insertion_buggy2 on {target}, returns {binary_search_insertion_buggy2(arr, target)}")
print(f"\n")

print(f"Third buggy implementation sets while left <= right:")
target = 4 # Correct impl should return 2 (inserted after 3)
print(f"Running binary_search_insertion_correct on {target}, returns {binary_search_insertion_correct(arr, target)}")
print(f"Running binary_search_insertion_buggy3 on {target}, returns {binary_search_insertion_buggy3(arr, target)}")
print(f"\n")

print(f"Another potential buggy implementation returns mid if arr[mid] == target")
target = 5 # Correct impl should return 2 (first occurence
print(f"Running binary_search_insertion_correct on {target}, returns {binary_search_insertion_correct(arr, target)}")
print(f"Running binary_search_insertion_maybebuggy on {target}, returns {binary_search_insertion_maybebuggy(arr, target)}")
print(f"\n")