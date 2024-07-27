import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, city_coordinates):
    total_cities = len(city_coordinates)
    visited = set()
    max_travel_cost = 0
    travel_costs = []
    
    # Verify each robot's tour
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at the depot city 0
        
        tour_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            distance = calculate_euclidean_distance(city_coordinates[city1], city_coordinates[city2])
            tour_cost += distance
            if city2 != 0:
                visited.add(city2)
        
        # Keep track of the highest tour cost
        max_travel_cost = max(max_travel_cost, tour_cost)
        travel_costs.append(tour_cost)
    
    # Check if all cities were visited once
    if len(visited) != total_cities - 1:
        return "FAIL"  # some cities may be visited more than once or not visited at all
    
    # Check reported maximum
    reported_max_cost = max(travel_costs)
    if reported_max_cost != max_travel_cost:
        return "FAIL"  # mismatch in the reported max cost
    
    return "CORRECT"

# Cities and their coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Tours provided in the solution
tours = [
    [0, 12, 14, 11, 1, 3, 2, 5, 18, 6, 0],
    [0, 17, 16, 8, 9, 15, 13, 7, 10, 4, 0]
]

# Verification of the solution
output = verify_solution(tours, city_coordinates)
print(output)