"""125. Valid Palindrome (leetcode)"""

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
