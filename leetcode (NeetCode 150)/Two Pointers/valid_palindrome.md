# 125. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Description**: Given a string `s`, check if it can be constructed into a palindrome after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

**Example 1**:

```
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: After cleaning and converting, the string becomes "amanaplanacanalpanama", which is a palindrome.
```

**Example 2**:

```
Input: s = "race a car"
Output: False
Explanation: After cleaning and converting, the string becomes "raceacar", which is not a palindrome.
```

**Two Pointer Approach**:

An approach that is frequently used for array and string problems is the two-pointer approach. Two pointers that travel in the same direction are used in this manner. Because we can compare characters from the beginning and end of the string, working our way inward and making sure that non-alphanumeric characters are skipped, it's especially helpful for this case. Here's a quick summary:

1. **Initialize Two Pointers**: One at the start (`left`) and the other at the end (`right`) of the string.
2. **Iterate Until The Pointers Meet**: While `left` is less than `right`, do the following:
   - Increment the `left` pointer if it's pointing to a non-alphanumeric character.
   - Decrement the `right` pointer if it's pointing to a non-alphanumeric character.
   - If the characters at the `left` and `right` pointers are different (case-insensitive), return False.
   - Move the pointers towards each other.
3. If the loop completes, return True.

**Python Code**:

```python
class Solution:
    """
    A class to solve the problem of checking if a string is a palindrome.
    Two pointer approch:
    Time complexity: O(n)
    Space complexity: O(1)
    """
    @staticmethod
    #Used @staticmethod for the is_alpha_num function since it doesn't depend on the instance state.
    def is_alpha_num(c: str) -> bool:
        """
        Checks if the given character is alphanumeric.
        
        Args:
        - c (str): The character to check.

        Returns:
        - bool: True if the character is alphanumeric, False otherwise.
        """
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def is_palindrome(self, sts: str) -> bool:
        """
        Determines if the string is a palindrome considering only alphanumeric characters.

        Args:
        - sts (str): The string to check.

        Returns:
        - bool: True if the string is a palindrome, False otherwise.
        """
        left, right = 0, len(sts) - 1

        while left < right:
            while left < right and not self.is_alpha_num(sts[left]):
                left += 1
            while right > left and not self.is_alpha_num(sts[right]):
                right -= 1
            if sts[left].lower() != sts[right].lower():
                return False
            left, right = left + 1, right - 1

        return True


if __name__ == "__main__":
    S = "A man, a plan, a canal: Panama"
    solution = Solution()
    print("is_palindrome:", solution.is_palindrome(S))

```

To check for palindromes, the algorithm uses the two-pointer approach and utilizes the helper function `is_alpha_num` to identify alphanumeric characters. The `is_palindrome` function then ensures that we're only comparing alphanumeric characters and that our comparison is case-insensitive.

By using this method, we can efficiently determine whether the string is a palindrome or not without needing any additional memory space (aside from the few variables used), hence achieving a space complexity of \(O(1)\).