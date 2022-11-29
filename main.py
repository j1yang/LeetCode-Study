num = 38

nums = list(str(num))
res = 0

if len(str(num)) == 1:
    print(num)
else:
    while len(nums) > 1:
        for i in nums:
            res += int(i)
            print(res)

        nums = list(str(res))
        res = 0
        if len(nums) == 1:
            print(int(nums[0]))