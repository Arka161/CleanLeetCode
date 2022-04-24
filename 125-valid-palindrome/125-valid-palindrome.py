class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_s = ""
        for i in s:
            if i.isalnum():
                final_s += i.lower()
        #print("Finals", final_s)
        return final_s == final_s[::-1]