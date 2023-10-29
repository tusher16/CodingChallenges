"""1. Two Sum Problem (leetcode)"""

def two_sum_bf(nums_list: list[int], target_value: int) -> list[int]:
    """Brute Force Approach
    Time complexity: O(n)  |  Space complexity: O(n)
    """
    numbers = {}
    for i, num in enumerate(nums_list):
        potential_match = target_value - num
        if potential_match in numbers:
            return [numbers[potential_match], i]
        numbers[num] = i
    return []


def two_sum_ht(nums_list: list[int], target_value: int) -> list[int]:
    """HashTable Approach
    Time complexity: O(n)  |  Space complexity: O(n)
    """
    numbers = {}
    for i, num in enumerate(nums_list):
        potential_match = target_value - num
        if potential_match in numbers:
            return [numbers[potential_match], i]
        numbers[num] = i
    return []


if __name__ == "__main__":
    NUMS_TEST = [2, 7, 11, 15]
    TARGET_TEST = 9

    print("Brute Force Approach:", two_sum_bf(NUMS_TEST, TARGET_TEST))
    print("Hash Table Approach:", two_sum_ht(NUMS_TEST, TARGET_TEST))
