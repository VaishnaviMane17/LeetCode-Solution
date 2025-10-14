class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        
        nums1.sort()

        n = len(nums1)

        if n%2 != 0:
            Median = nums1[(n//2)]
        else:
            Median = (nums1[(n//2) - 1] + nums1[(n//2)]) / 2        
        return Median