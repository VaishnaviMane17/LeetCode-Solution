class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for ele in words:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1

        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key)) 

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

