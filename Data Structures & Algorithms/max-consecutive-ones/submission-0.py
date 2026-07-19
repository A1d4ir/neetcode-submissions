class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count = 0
        current_ones_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current_ones_count += 1;
            else:
                if current_ones_count > ones_count:
                    ones_count = current_ones_count
                current_ones_count = 0
            
            if i == len(nums) - 1 and current_ones_count > ones_count:
                ones_count = current_ones_count

        return ones_count