class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        pos_speed = sorted(pos_speed, key=lambda x : x[0])
        
        last_arrival = None
        
        results = 0
        while pos_speed:
            next_car_pos, next_car_speed = pos_speed.pop()
            arrival_time = (target - next_car_pos) / next_car_speed
            if not last_arrival or last_arrival < arrival_time:
                results += 1
                last_arrival = arrival_time
        return results