class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        median = 0
        medianID = len(nums)//2
        if len(nums)%2 == 0:
            if(nums[medianID-1] != nums[medianID]):
                if((nums[medianID-1]+nums[medianID])%2 == 0):
                    median = (nums[medianID-1]+nums[medianID])/2 
                else:
                    median = (nums[medianID-1]+nums[medianID])/2 + 0.5
            else:
                median = nums[medianID]
        else:
            median = float(nums[medianID])
        return median
