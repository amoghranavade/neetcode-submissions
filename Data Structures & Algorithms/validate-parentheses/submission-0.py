class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        open_close_map_dict = {"}": "{", ")": "(", "]": "["}

        for i in s:
            if i in open_close_map_dict:
                if not my_stack or my_stack[-1] != open_close_map_dict[i]:
                    return False
                my_stack.pop()
            else:
                my_stack.append(i)

        return len(my_stack) == 0