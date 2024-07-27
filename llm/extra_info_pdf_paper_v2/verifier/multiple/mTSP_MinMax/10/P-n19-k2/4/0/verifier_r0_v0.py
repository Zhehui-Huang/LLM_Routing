import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, max_travel_cost, coordinates):
    # Verify Requirement 1: Check coordinates match for 19 cities
    if len(coordinates) != 19:
        return "FAIL"
    
    visited = set()
    actual_max_cost = 0
    
    for tour in tours:
        # Verify Requirement 2: Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate travel distance
        travel_cost = 0
        for i in range(len(tour) - 1):
            travel_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
            visited.add(tour[i+1])
        
        # Track the max cost
        actual_max_cost = max(actual_max_cost, travel_cost)
        
        # Verify Requirement 6: Tour output includes total cost close to the provided with some tolerance (floating point operations)
        if not math.isclose(travel_cost, tours[tour]['cost'], rel_tol=1e-5):
            return "FAIL"
    
    # Verify Requirement 4: Each city except depot visited exactly once
    if len(visited) != 18 or any(city not in visited for city in range(1, 19)):
        return "FAIL"
    
    # Verify Requirement 5: Minimize the maximum distance
    if not math.isclose(max_travel_cost, actual_max_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Solution provided
tours = {
    (0, 18, 7, 9, 6, 2, 16, 5, 15, 13, 0): 164.44130216183953,
    (0, 10, 1, 11, 4, 17, 8, 14, 12, 3, 0): 170.4398813821195
}

status = verify_solution(tours, 170.4398813821195, coordinates)
print(status)