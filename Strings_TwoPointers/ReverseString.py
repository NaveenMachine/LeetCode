class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        newList = list()

        Pointer1 = 0
        Pointer2 = len(s) - 1

        # Swap In Place
        while Pointer1 < Pointer2:
            s[Pointer1], s[Pointer2] = s[Pointer2], s[Pointer1]
            Pointer1 += 1
            Pointer2 -= 1
        
        
        