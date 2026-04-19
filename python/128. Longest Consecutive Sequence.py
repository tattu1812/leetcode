class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr = num
                length = 1

                while curr + 1 in numSet:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest
        