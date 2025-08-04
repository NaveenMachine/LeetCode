class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = []
        postfix = []

        prefixTotal = 1
        for num in nums:
            prefixTotal *= num
            prefix.append(prefixTotal)

        postfixTotal = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixTotal *= nums[i]
            postfix.append(postfixTotal)
        postfix.reverse()

        for j in range(len(nums)):
            preNum = 1
            postNum = 1
            if (j - 1) >= 0:
                preNum = prefix[j - 1]
            if (j + 1) < (len(nums)):
                postNum = postfix[j + 1]
            result.append(preNum * postNum)

        return result
