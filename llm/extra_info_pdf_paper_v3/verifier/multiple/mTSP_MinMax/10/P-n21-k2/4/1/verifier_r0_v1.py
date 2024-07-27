import math

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Solution given for tours and costs
tours = [
    {'tour': [0, 1, 10, 8, 18, 19, 3, 12, 15, 11, 4, 0], 'cost': 116.33},
    {'tour': [0, 6, 20, 5, 14, 17, 9, 13, 7, 2, 16, 0], 'cost': 96.66}
]
max_cost = 116.33

def test_solution(cities, tours, max_cost):
    all_visited = set()
    
    # Test each tour
    for tour_info in tours:
        # Extract information correctly
        tour = tour_info['tour']
        cost = tour_info['cost']
        expected_cost = 0
    
        # Check returns to depot and starts from depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
        # Calculate expected cost and collect visited cities
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                all_visited.add(tour[i])
            distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            expected_cost += distance
    
        # Compare expected and actual costs, allow for minor floating-point inaccuracies
        if not math.isclose(cost, expected_cost, abs_tol=0.5):
            return "FAIL"
    
    # Check if all cities except the depot were visited exactly once
    if len(all_visited) != len(cities) - 1:
        return "FAIL"
    
    # Check the maximum reported cost
    actual_max_cost = max([t['cost'] for t in tours])
    if not math.isclose(actual_max_cost, max_cost, abs_tol=0.5):
        return "FAIL"
    
    return "CORRECT"

# Output from the test function
print(test_solution(cities, tours, max_cost))