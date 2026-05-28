class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        array_dict = {}

        for i in range(0, len(nums)):
            if nums[i] in array_dict:
                return True

            else:
                array_dict[nums[i]] = 1

        return False
        