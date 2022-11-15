# 13. Roman to Integer


def romanToInt(self, s: str) -> int:
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    romans = list(s)

    def intList(r):
        match r:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000

    ints = map(intList, romans)

    return sum(list(ints))


# 1. Two Sum


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]


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