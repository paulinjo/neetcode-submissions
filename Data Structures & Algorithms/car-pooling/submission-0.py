from collections import namedtuple, deque
import heapq

NewTrip = namedtuple('NewTrip', ['source', 'dest', 'num_passengers'])
ActiveTrip = namedtuple('ActiveTrip', ['dest', 'num_passengers'])

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        new_trips = [NewTrip(source=t[1], dest=t[2], num_passengers=t[0]) for t in trips]
        active_trips = []
        current_passengers = 0

        heapq.heapify(active_trips)
        new_trips = deque(sorted(new_trips))

        while new_trips:
            next_trip = new_trips.popleft()

            while active_trips and active_trips[0].dest <= next_trip.source:
                completed_trip = heapq.heappop(active_trips)
                current_passengers -= completed_trip.num_passengers
            
            current_passengers += next_trip.num_passengers
            if current_passengers > capacity:
                return False

            heapq.heappush(active_trips, ActiveTrip(dest=next_trip.dest, num_passengers=next_trip.num_passengers))
            

        return True