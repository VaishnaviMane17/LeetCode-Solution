class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heap = [-num for num in piles]
        heapq.heapify(heap)
        ct = 0
        while ct<k:
            x = abs(heapq.heappop(heap))
            heapq.heappush(heap,-(x-(x//2)))
            ct += 1
        piles = (-num for num in heap)

        return sum(piles)



        