# Two Sum solved using the Two Pointer Algorithm.
# Runtime: O(n)

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type targer: int
    :rtype: List[int]
    """
    # Create a list of nums and their index [(0, num0), (1, num1)]
    indexed_nums = list(enumerate(nums))
    # Sort the list based on the numbers
    indexed_nums.sort(key=lambda x: x[1])

    pointer1 = 0
    pointer2 = len(indexed_nums) - 1

    while pointer1 < pointer2:
        num1 = indexed_nums[pointer1][1]
        num2 = indexed_nums[pointer2][1]
        total = num1 + num2

        if total == target:
            return [indexed_nums[pointer1][0], indexed_nums[pointer2][0]]
        elif total < target:
            pointer1 += 1
        else:
            pointer2 -= 1
