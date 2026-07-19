class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans_len = nums_len * 2
        ans = [0] * ans_len

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[nums_len + i] = nums[i]
        
        return ans