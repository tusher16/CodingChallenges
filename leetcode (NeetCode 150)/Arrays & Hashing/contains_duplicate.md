# 217. Contains Duplicate

**Description**: Given an array of integers, determine if it contains any duplicates.

Your function should return `true` if any value appears at least twice in the array, and it should return `false` if every element is distinct.

---

## Example:

```python
Input: [1,2,3,1]
Output: True
```

```python
Input: [1,2,3,4]
Output: False
```

---

## Brute Force Approach:

The idea is to compare each number with every other number in the array.

**Steps**:

1. Loop over each number in the array.
2. For each number, loop over all subsequent numbers.
3. Compare if the two numbers are equal.

If you find two numbers that are the same, then there are duplicates in the array. Otherwise, there are no duplicates.

**Python Code**:

```python
def has_duplicate_bf(nums_list):
    for i in range(len(nums_list) - 1):
        for j in range(i + 1, len(nums_list)):
            if nums_list[i] == nums_list[j]:
                return True
    return False
```

This approach achieves a time complexity of `O(n^2)` and a space complexity of `O(1)`.

---

## Sort and Compare Approach:

By sorting the array first, all duplicate numbers will be next to each other. Hence, by comparing each number to its next neighbor, you can easily identify duplicates.

**Steps**:

1. Sort the array.
2. Loop over the array and compare each number to its next neighbor.

**Python Code**:

```python
def has_duplicate_s(nums_list):
    nums_list.sort()
    for i in range(1, len(nums_list)):
        if nums_list[i] == nums_list[i - 1]:
            return True
    return False
```

This approach achieves a time complexity of `O(nlogn)` (due to the sort operation) and a space complexity of `O(1)`.

---

## HashSet Approach:

Use a set to store numbers as you iterate over the array. If a number is already in the set, then it's a duplicate.

**Steps**:

1. Initialize an empty set.
2. Loop over the array.
3. For each number, check if it's in the set.
4. If it's in the set, return `True`. If not, add it to the set.

**Python Code**:

```python
def has_duplicate_hs(nums_list):
    seen_numbers = set()
    for num in nums_list:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False
```

This approach achieves a time complexity of `O(n)` and a space complexity of `O(n)`.

---

## Testing:

To check the validity of our solutions, let's test them:

```python
if __name__ == "__main__":
    NUMS_TEST = [1, 2, 3, 2]
    print("Brute Force Approach:", has_duplicate_bf(NUMS_TEST))
    print("Sort and Compare Approach:", has_duplicate_s(NUMS_TEST))
    print("HashSet Approach:", has_duplicate_hs(NUMS_TEST))
```

This will give us an output of `True` for all three methods, indicating that the array `[1, 2, 3, 2]` indeed has duplicates.