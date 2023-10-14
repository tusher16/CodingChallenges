#1st Approach: Brute force
# Time complexity O(nlogn) space complexity
def two_Sum_BF(nums, target):
    numbers = {}
    for i, num in enumerate(nums):
        potentialmatch = target - num
        if potentialmatch in numbers:
            return [numbers[potentialmatch], i]
        else:
            numbers[num] = i
    return []


#2nd Approach: HashTable,
#Time complexity O(n^2) space complexity O(n)
def two_Sum_HT(nums, target):
    numbers = {}
    for i, num in enumerate(nums):
        potentialmatch = target - num
        if potentialmatch in numbers:
            return [numbers[potentialmatch], i]
        else:
            numbers[num] = i
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    
    print("Brute Force Approch: ",two_Sum_BF(nums, target))
    print("Hash Table Approch: ", two_Sum_HT(nums, target))