import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

robot_tours = [
    [0, 12, 14, 15, 16, 18, 0],
    [0, 3, 4, 6, 8, 10, 11, 0],
    [0, 13, 17, 19, 20, 21, 0],
    [0, 1, 2, 5, 7, 9, 0]
]

# Calculate total travel cost
reported_costs = [121.21, 124.24, 138.25, 111.84]
calculated_costs = []

def test_all_visited_exactly_once_and_costs():
    all_cities_visited = set()
    total_calculated_cost = 0
    
    for tour, reported_cost in zip(robot_tours, reported_costs):
        # Check if tours start and end at the depot city
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        tour_cost = 0
        # Calculate cost and update visited cities
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                all_cities_visited.add(tour[i])
            city1 = cities[tour[i]]
            city2 = cities[tour[i + 1]]
            tour_cost += calculate_distance(city1, city2)
        
        total_calculated_cost += tour_cost
        calculated_costs.append(round(tour_cost, 2))
        if not math.isclose(tour_cost, reported_cost, abs_tol=0.1):
            return "FAIL"
    
    # Check if all cities except depot are visited
    if all_cities_visited != set(cities.keys()) - {0}:
        return "FAIL"
    
    # Check total cost
    if not math.isclose(total_calculated_cost, sum(reported_costs), abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Print the test result
print(test_all_visited_exactly_once_and_costs())