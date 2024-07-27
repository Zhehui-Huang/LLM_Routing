import math

# Given tours and their cost
tours = {
    0: ([0, 1, 2, 0], 52.491761791689186),
    1: ([0, 3, 4, 0], 52.491761791689186),
    2: ([0, 5, 6, 0], 52.491761791689186),
    3: ([0, 7, 8, 0], 52.491761791689186),
    4: ([0, 9, 10, 0], 52.491761791689186),
    5: ([0, 11, 12, 0], 52.491761791689186),
    6: ([0, 13, 14, 0], 52.491761791689186),
    7: ([0, 15, 16, 0], 52.491761791689186),
    8: ([0, 17, 18, 0], 52.491761791689186),
    9: ([0, 19, 20, 0], 52.491761791689186),
    10: ([0, 21, 22, 0], 52.491761791689186)
}

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Function to calculate the distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if the total travel cost is correct and each city is visited only once
def verify_solution(tours):
    all_visited_cities = set()
    total_calculated_cost = 0.0
    
    for tour, reported_cost in tours.values():
        calculated_cost = 0.0
        previous_city = tour[0]
        
        # Check if each robot starts from the designated depot (Requirement 2)
        if previous_city != 0:
            return "FAIL"
        
        for city in tour[1:]:
            if city in all_visited_cities:
                return "FAIL"  # Each city should be visited once (Requirement 1)
            all_visited_cities.add(city)
            calculated_cost += calculate_distance(previous_city, city)
            previous_city = city
        
        # Checking if start and end point is the depot city
        if previous_city != 0:
            return "FAIL"  # Must end at the depot city (Requirement 3)
        
        if calculated_cost != reported_cost:
            return "FAIL"  # Check if the reported tour cost matches the calculated cost
        
        total_calculated_series =+ visited_cost

    total_reported_cost = sum(cost for _, cost in tours.values())
    
    if abs(total_calculated_series - 790.8742071900735) > 1e-6:
        return "FAIL"  # Check the total travel cost (Requirement 4)

    return "CORRECT"

# Run verification
result = verify_solution(tours)
print(result)