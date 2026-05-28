import heapq

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

        

            top_k_pairs = heapq.nlargest(
                k,
                hash_map.items(),
                key=lambda x: x[1]
            )

            top_k_keys = []

            for key, value in top_k_pairs:
                top_k_keys.append(key)


        # print(unique)
        return top_k_keys