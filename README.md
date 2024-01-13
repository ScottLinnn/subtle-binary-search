# subtle-binary-search

I found writing binary search is error-prone, especially when it's interacting with other parts in a large complicated problem. 
Understanding every piece of the bianry search code is crucial to get it right.

## binary_search_insertion

Showing potential bugs when writing binary search to find the insertion position.

Subtleness includes:  
- right = mid VS right = mid-1  
- right = len(arr) VS right = len(arr)-1  
- while left < right VS while left <= right  
- if arr[mid] == target: return mid VS right = mid  

```
First buggy implementation sets right = mid-1
Running binary_search_insertion_correct on 2, returns 1
Running binary_search_insertion_buggy1 on 2, returns 0


Second buggy implementation sets right = len(arr) - 1
Running binary_search_insertion_correct on 10, returns 6
Running binary_search_insertion_buggy2 on 10, returns 5


Third buggy implementation sets while left <= right:
Running binary_search_insertion_correct on 4, returns 2
binary_search_insertion_buggy3 has run loop 1k times!
Running binary_search_insertion_buggy3 on 4, returns -1


Another potential buggy implementation returns mid if arr[mid] == target
Running binary_search_insertion_correct on 5, returns 2
Running binary_search_insertion_maybebuggy on 5, returns 3
```
