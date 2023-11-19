# [704. Binary Search](https://leetcode.com/problems/binary-search/)

**Description**: Given a 1-indexed array of integers `nums` that is already sorted in non-decreasing order, find the index of a given integer `target` in the array. If `target` is not present in the array, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1**:

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

**Example 2**:

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

**Constraints**:

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are unique.
- `nums` is sorted in non-decreasing order.

---

**Binary Search Approach**:

Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item until you've narrowed the possible locations to just one. Here is the general idea:

1. **Initialize Pointers**: Start with two pointers representing the lower and upper bounds of the list.

2. **Iterate and Divide**: Compare the target to the middle element of the bounds.
   - If the target is equal to the middle element, return the index.
   - If the target is less, move the upper bound to just below the middle element.
   - If the target is more, move the lower bound to just above the middle element.

3. **Result**: Continue the process until the target is found or the bounds converge, indicating the target is not present.

**Python Solution**:

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

# Test
nums = [-1,0,3,5,9,12]
target = 2
solution = Solution()
print("Output:", solution.search(nums, target))
```

This solution has a time complexity of `O(log n)`, where `n` is the number of elements in the array, as the search space is halved with each step. The space complexity is `O(1)` as it operates in place without requiring additional space proportional to the input size.

## Note
Binary Search requires the input list to be sorted and uses a divide-and-conquer strategy to locate the target index efficiently.
