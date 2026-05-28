class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_dict = {}

        for i in s:

            if i in ana_dict:
                count = ana_dict[i]
                ana_dict[i] = count + 1

            else:
                ana_dict[i] = 1

        for j in t:

            if j in ana_dict:
                count = ana_dict[j] 
                ana_dict[j] = count - 1

            else:
                return False

        for value in ana_dict.values():
            if value != 0:
                return False
        return True
        # result = all(value == 0 for value in ana_dict.values())
        # return result

        