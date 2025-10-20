from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        freq = Counter(s)

        heap = [(-ord(ch), ch, c) for ch, c in freq.items()]
        heapq.heapify(heap)
        result = []
        
        while heap:
            neg_ord1, ch1, c1 = heapq.heappop(heap)
            times = min(c1 , repeatLimit)
            result.append(ch1 * times)
            c1 -= times

            if c1 == 0:
                continue
            
            if not heap:
                break
            
            neg_ord2, ch2, c2 = heapq.heappop(heap)
            result.append(ch2)
            c2 -= 1

            if c2 > 0:
                heapq.heappush(heap , (neg_ord2, ch2, c2))

            heapq.heappush(heap, (neg_ord1, ch1, c1))

        return "".join(result)
        