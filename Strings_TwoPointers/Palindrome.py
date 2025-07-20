class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = ''.join(c for c in s.lower() if c.isalnum())

        pointer1 = 0
        pointer2 = len(check) - 1

        while pointer1 < pointer2:
            if(check[pointer1] != check[pointer2]):
                return False
            else:
                pointer1 += 1
                pointer2 -= 1

        return True
        