class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-num for num in nums]
        heapq.heapify(nums)
        i = 0

        while i < k :
            ans = heapq.heappop(nums)
            i += 1
        
        return -ans
