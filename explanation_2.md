Implement the search algorithm in rotated sorted array.
Have to find the given number and to do it in log(n) time.

Solution which come to mind is binary search but the given array is not sorted array, but rotated sorted array.
So, to find the pivot from where it is rotated.
So, have found the pivot first, i.e. by how much amount the sorted array is shifted.
Then in the two divided part, we have implemented the binary search directly.

Time Complexity: O(log(n))
Space Complexity: O(1)
