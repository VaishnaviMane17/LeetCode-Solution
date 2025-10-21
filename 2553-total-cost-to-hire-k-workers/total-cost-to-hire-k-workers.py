import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total = 0

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Initialize both heaps with up to `candidates` elements
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        for _ in range(k):
            # Pick the worker with the smaller cost, break ties by index
            if left_heap and right_heap:
                if left_heap[0][0] < right_heap[0][0]:
                    cost, _ = heapq.heappop(left_heap)
                    total += cost
                    if left <= right:
                        heapq.heappush(left_heap, (costs[left], left))
                        left += 1
                elif left_heap[0][0] > right_heap[0][0]:
                    cost, _ = heapq.heappop(right_heap)
                    total += cost
                    if left <= right:
                        heapq.heappush(right_heap, (costs[right], right))
                        right -= 1
                else:
                    # Tie in cost, break by index
                    if left_heap[0][1] <= right_heap[0][1]:
                        cost, _ = heapq.heappop(left_heap)
                        total += cost
                        if left <= right:
                            heapq.heappush(left_heap, (costs[left], left))
                            left += 1
                    else:
                        cost, _ = heapq.heappop(right_heap)
                        total += cost
                        if left <= right:
                            heapq.heappush(right_heap, (costs[right], right))
                            right -= 1
            elif left_heap:
                cost, _ = heapq.heappop(left_heap)
                total += cost
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            elif right_heap:
                cost, _ = heapq.heappop(right_heap)
                total += cost
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total
