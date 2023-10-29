"""
217. Contains Duplicate (leetcode)
"""

def has_duplicate_bf(nums_list: list[int]) -> bool:
    """
    Brute force approach to check for duplicates.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i in range(len(nums_list) - 1):
        for j in range(i + 1, len(nums_list)):
            if nums_list[i] == nums_list[j]:
                return True
    return False


def has_duplicate_s(nums_list: list[int]) -> bool:
    """
    Sort then search approach to check for duplicates.
    Time complexity: O(nlogn)
    Space complexity: O(1)
    """
    nums_list.sort()
    for i in range(1, len(nums_list)):
        if nums_list[i] == nums_list[i - 1]:
            return True
    return False


def has_duplicate_hs(nums_list: list[int]) -> bool:
    """
    Hash Set approach to check for duplicates.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen_numbers = set()
    for num in nums_list:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False


if __name__ == "__main__":
    NUMS_TEST = [1, 2, 3, 2]
    print("Brute Force Approach:", has_duplicate_bf(NUMS_TEST))
    print("Sort Approach:", has_duplicate_s(NUMS_TEST))
    print("HashSet Approach:", has_duplicate_hs(NUMS_TEST))
