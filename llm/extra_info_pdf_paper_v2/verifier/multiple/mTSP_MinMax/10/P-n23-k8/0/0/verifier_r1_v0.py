import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tours(tours, costs, cities):
    max_cost = max(costs)
    city_visited = set()
    for tour, cost in zip(tours, costs):
        # Check if each robot starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check if cities except depot are visited exactly once
        for city in tour[1:-1]:
            if city in city_visited:
                return "FAIL"
            city_visited.add(city)
    
    # All cities except the depot must be visited exactly once
    if len(city_visited) != len(cities) - 1:
        return "FAIL"
    
    # Check the accuracy of given tour costs
    for tour, cost in zip(tours, costs):
        computed_cost = 0
        for i in range(len(tour) - 1):
            computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        if not math.isclose(computed_cost, cost, rel_tol=1e-6):
            return "FAIL"
    
    return "CORRECT"

# Cities (only indexes, the coordinates are supposed to be pre-determined)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Given solution details
tours = [
    [0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 0], [0, 7, 8, 0], [0, 9, 10, 0],
    [0, 11, 12, 0], [0, 13, 14, 0], [0, 15, 16, 0]
]
costs = [47.28555690793142, 75.67537984747364, 47.93463581488838, 72.1927221713905, 
         77.87109113044761, 74.15812335008223, 80.99113763798833, 62.85459664679527]

# Verify solution
result = verify_tours(tours, costs, cities)
print(result)