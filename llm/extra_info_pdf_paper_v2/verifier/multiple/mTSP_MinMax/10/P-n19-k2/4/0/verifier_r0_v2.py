import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, max_travel_cost, coordinates):
    if len(coordinates) != 19:
        return "FAIL"
    
    visited = set()
    actual_max_cost = 0

    for tour, reported_cost in tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate the travel cost for the tour
        travel_cost = 0
        for i in range(1, len(tour)):
            travel_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
            visited.add(tour[i])
        
        # Check if the calculated travel cost matches the reported cost
        actual_max_cost = max(actual_max_totals_cost, travel_cost)
        if not math.isclose(travel_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"
    
    # All cities (except depot) must be visited exactly once
    if len(visited) != 18 or any(i not in visited for i in range(1, 19)):
        return "FAIL"
    
    # Check maximum travel cost is minimized (matches the provided max_travel_cost)
    if not math.isclose(max_travel_cost, actual_max_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Submitted solution with costs
tours = {
    (0, 18, 7, 9, 6, 2, 16, 5, 15, 13, 0): 164.44130216183953,
    (0, 10, 1, 11, 4, 17, 8, 14, 12, 3, 0): 170.4398813821195
}

status = verify_solution(tours, 170.4398813821195, coordinates)
print(status)