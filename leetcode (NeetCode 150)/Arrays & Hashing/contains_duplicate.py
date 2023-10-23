#1st Approach: Brute force
# Time complexity O(n^2) 
# space complexity O(1) 
def has_duplicate_bf(nums):
    numbers = {}
    for i in range(len(nums)-1):
        f_num = nums[i]
        for j in range(i+1, len(nums)):
            s_num = nums[j]
            if f_num == s_num:
                return True
    return False

#1st Approach: Sort then search
# Time complexity O(nlogn)
# space complexity O(1)
def has_duplicate_s(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

#1st Approach: Hash Set
# Time complexity O(n)
# space complexity O(n)
def has_duplicate_hs(nums):
    numbers = {}
    for i in range(len(nums)-1):
        f_num = nums[i]
        for j in range(i+1, len(nums)):
            s_num = nums[j]
            if f_num == s_num:
                return True
    return False

if __name__ == "__main__":
    nums = [1, 2, 3, 2]
    print("Brute Force Approch: ",has_duplicate_bf(nums))
    print("sort Approch: ", has_duplicate_s(nums))
    print("HashSet Approch: ", has_duplicate_hs(nums))