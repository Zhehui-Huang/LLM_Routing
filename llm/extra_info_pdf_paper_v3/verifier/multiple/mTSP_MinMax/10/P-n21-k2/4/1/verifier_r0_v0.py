import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Solution provided
tours = [
    {'tour': [0, 1, 10, 8, 18, 19, 3, 12, 15, 11, 4, 0], 'cost': 116.33},
    {'tour': [0, 6, 20, 5, 14, 17, 9, 13, 7, 2, 16, 0], 'cost': 96.66}
]
max_cost = 116.33

def test_solution(cities, tours, max_cost):
    all_visited = set()
    
    # Test each tour
    for tour_info in tours:
        tour = tour /tour_info['tour']
        cost = tour_info['cost']
        expected_cost = 0
        
        # Check return to depot and starts from depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate expected cost and collect visited cities
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                all_visited.add(tour[i])
            distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            expected_cost += distance
        
        # Check if the cost is approximately correct, allowing for minor floating point errors
        if not math.isclose(cost, expected_cost, abs_tol=0.01):
            return "FAIL"
    
    # Check if all cities are visited exactly once
    if len(all_visited) != 20:
        return "FAIL"
    
    # Check the maximum cost
    actual_max_cost = max([tour_info['cost'] for tour in tour_info])
    if not math.isclose(actual_max_cost, max_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_solution(cities, tours, max_cost))