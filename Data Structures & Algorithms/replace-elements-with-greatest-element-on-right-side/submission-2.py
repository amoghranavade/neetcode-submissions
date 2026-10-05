class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        curr_max = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, temp)

        # for i in range(0, len(arr)):
        #     curr_max = -1
        #     for j in range(i+1, len(arr)):
    
        #         if arr[j] > curr_max:
        #             curr_max = arr[j]

        #     # print(curr_max)
        #     arr[i] = curr_max
        #     # curr_max = 0
        return arr
              

        