class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        total = sum(piles)
        heap = [-num for num in piles]
        heapq.heapify(heap)
        

        for i in range(k):
            largest = abs(heapq.heappop(heap))
            stone = floor(largest/2)
            total -= stone
            heapq.heappush(heap, -(largest-stone))
        
        return total


        