Certainly! Here's a text representation of the image for a `README.md`:

---

# LeetCode - Arrays and Hashing

## 1.[Two Sum](https://leetcode.com/problems/two-sum/submissions/1065824850/)

**Description**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

**Example 1**:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explain: Because nums[0] + nums[1] == 9, we return [0,1]
```

**Example 2**:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Brute force**:

Brute force is a straightforward method to solve a problem, usually directly based on the problem's statement and definitions. Here's a simple breakdown of the brute-force approach you provided in your Python solution:

1. **Loop Over Each Number:**
   - We start by looping over each number in the array with one loop. Let's call the number we select in this loop `first_num`.

2. **Loop Over the Rest of the Numbers:**
   - For each `first_num`, we loop over all the other numbers in the array with a second loop. Let's call the number we select in the second loop `second_num`.

3. **Check Their Sum:**
   - We check whether `first_num` + `second_num` equals `target`. If it does, we've found our two numbers!

4. **Return the Indices:**
   - If we find two numbers that add up to `target`, we return their indices in the array.

**Python Solution**:

```python
# Loop over each number in the array.
for i in range(len(nums) - 1):  # i goes from 0 to the second-last index.
    first_num = nums[i]  # Select a number.

    # Loop over all the other numbers.
    for j in range(i+1, len(nums)):  # j goes from i+1 to the last index.
        second_num = nums[j]  # Select another number.

        # Check if the two numbers add up to the target.
        if first_num + second_num == target:
            return [i, j]  # If they do, return their indices.
```

This approach achieves a time complexity of `O(n^2)` and a space complexity of `O(1)`.

---

## 2nd Approach:

For an array `[3,5,-4,8,11,1,-1,6]` with a `target` of `10`, the algorithm will process as follows:

**Steps**:

`target` = `10`, 
`current_sum` = `x`

if `x + y = 10`, then `y = 10 - x`

1. For `x = 3`, then `y = 10 - 3 ` ` = 7`
2. For `x = 5`, then `y = 10 - 5 ` ` = 5`
3. For `x = -4`, then `y = 10 - (-4) ` ` = 14`
4. For `x = 8`, then `y = 10 - 8 ` ` = 2`
5. For `x = 11`, then `y = 10 - 11 ` ` = 1`
6. For `x = 1`, then `y = 10 - 1 ` ` = 11` (Found in hash table)


**Hash Table Approach**:

As we iterate over the array, we keep track of the numbers seen in a hash table. This helps in achieving constant time look-up.

| Iteration | Hash Map Content            |
| --------- | --------------------------- |
| 1         | {3:True}                    |
| 2         | {3:True, 5:True}            |
| 3         | {3:True, 5:True, -4:True}    |
| 4         | {3:True, 5:True, -4:True}    |
| 5         | {3:True, 5:True, -4:True, 8:True} |
| 6         | {3:True, 5:True, -4:True, 8:True, 11:True} |
| 7         | {3:True, 5:True, -4:True, 8:True, 11:True, 1:True} |

**Python Code**:

```python
numbers = {}

for i, num in enumerate(nums):
    potential_match = target - num

    if potential_match in numbers:
        return [numbers[potential_match], i]
    else:
        numbers[num] = i

return []
```

This approach achieves a time complexity of `O(n)` and a space complexity of `O(n)`.

---
