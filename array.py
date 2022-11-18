class Solution:
  #136
  def singleNumber(self, nums: List[int]) -> int:
    return 2*(sum(set(nums)))-sum(nums)
  #169
  def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]
  #217
  def containsDuplicate(self, nums: List[int]) -> bool:
    if len(set(nums)) == len(nums):
        return False
    else:
        return True