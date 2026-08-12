class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0, len(people) - 1
        
        required_boats = 0
        current_boat_weight = 0
        current_boat_passengers = 0
        while i <= j:
            heaviest, lightest = people[j], people[i]
            if current_boat_passengers == 2:
                required_boats += 1
                current_boat_weight = 0
                current_boat_passengers = 0
            if current_boat_weight + heaviest <= limit:
                current_boat_weight += heaviest
                current_boat_passengers += 1
                j -= 1
            elif current_boat_weight + lightest <= limit:
                current_boat_weight += lightest
                current_boat_passengers += 1
                i += 1
            else:
                required_boats += 1
                current_boat_weight = 0
                current_boat_passengers = 0

        if current_boat_passengers:
            required_boats += 1

        return required_boats