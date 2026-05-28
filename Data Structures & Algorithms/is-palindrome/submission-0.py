class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        check = []

        for i in s:
            if not i.isalnum():
                continue

            check.append(i)

        dupli = check
        dupli = dupli[::-1]

        if check == dupli:
            return True
        return False
