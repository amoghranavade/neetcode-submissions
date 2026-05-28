class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            if nums[i] in hash_map:
                current_count = hash_map[nums[i]]
                new_count = current_count + 1

                hash_map[nums[i]] = new_count

            else:

                hash_map[nums[i]] = 1

        sorted_dict = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
        unique = list(sorted_dict.keys())[:k]
        # print(unique)
        return unique