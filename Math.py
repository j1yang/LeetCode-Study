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

#202
def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in memo:
                return False
            else:
                memo.add(n)
        else:
            return True

#168
def convertToTitle(self, columnNumber: int) -> str:
        # Create an empty string for storing the characters...
        output = ""
        while columnNumber > 0:
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26
        return(output)

#258
def addDigits(self, num: int) -> int:
    nums = list(str(num))
    res = 0

    if len(str(num)) == 1:
        return num
    else:
        while len(nums) > 1:
            for i in nums:
                res += int(i)

            nums = list(str(res))
            res = 0
            if len(nums) == 1:
                return int(nums[0])
#or. .. ... .
def addDigits(self, num: int) -> int:
        return num if num == 0 else num % 9 or 9

#7
def reverse(self, x: int) -> int:
        if int(str(abs(x))[::-1]) > 2**31:
            return 0

        return int(str(x)[::-1]) if x > 0 else (-1)*int(str(abs(x))[::-1])