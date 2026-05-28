class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #nums = [3,4,5,6]
        arr_dict = {}

        for i in range(0, len(nums)):
            # nums[i]
            to_check = target - nums[i]
            if to_check in arr_dict:
                indx_num = arr_dict[to_check]
                return [i, indx_num][::-1]

            else:
                arr_dict[nums[i]] = i

        