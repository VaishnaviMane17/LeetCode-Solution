import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1, n + 1))  # all seats available initially
        heapq.heapify(self.seats)
        self.reserved_set = set()  # track reserved seats if needed

    def reserve(self) -> int:
        seat = heapq.heappop(self.seats)
        self.reserved_set.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        self.reserved_set.discard(seatNumber)  # safe removal
        heapq.heappush(self.seats, seatNumber)

        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)