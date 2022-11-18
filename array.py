class Solution:
  #136
  def singleNumber(self, nums: List[int]) -> int:
    return 2*(sum(set(nums)))-sum(nums)
  #169
  def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]