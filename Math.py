# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1]

# 69
    def mySqrt(self, x: int) -> int:
        return math.floor(sqrt(x))

# 67

    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1

        if digits[-1] != 10:
            return digits

        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 10:
                if i != 0:
                    digits[i] = 0
                    digits[i-1] = digits[i-1] + 1
            elif digits[i] != 10:
                return digits

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
            return digits

        return digits
