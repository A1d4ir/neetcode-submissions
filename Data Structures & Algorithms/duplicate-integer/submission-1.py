class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        readedNums = set()
        for num in nums:
            if num in readedNums:
                return True
            readedNums.add(num)
        return False