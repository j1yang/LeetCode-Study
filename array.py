class Solution:
  #136
  def singleNumber(self, nums: List[int]) -> int:
    return 2*(sum(set(nums)))-sum(nums)