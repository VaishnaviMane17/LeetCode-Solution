class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.added = []
        self.added_set = set()

    def popSmallest(self) -> int:
        if self.added:
            val = heapq.heappop(self.added)
            self.added_set.remove(val)
            return val
        else:
            val = self.current
            self.current += 1
            return val

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_set:
             heapq.heappush(self.added, num)
             self.added_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)