import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(cities, tours, calculated_costs):
    # Verify that each robot starts and ends at the depot
    if not all(tour[0] == 0 and tour[-1] == 0 for tour in tours):
        return "FAIL"

    # Verify that all cities except the depot are visited exactly once
    visited_cities = [city for tour in tours for city in tour[1:-1]]
    if set(visited_cities) != set(range(1, 22)):
        return "FAIL"

    # Verify correct calculation of travel costs
    total_calculated_cost = 0
    for tour, cost in zip(tours, calculated_costs):
        compute_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            compute_cost += calculate_euclidean_heuristic_distance(cities[city1], cities[city2])
        total_calculated_cost += compute_cost
        if not math.isclose(compute_cost, cost, rel_tol=1e-5):
            return "FAIL"

    # Verify sum of individual costs matches reported total cost
    reported_total_cost = sum(calculated_costs)
    if not math.isclose(total_calulated_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given city coordinates: city_index: (x, y)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Given tours and costs
tours_and_costs = [
    ([0, 4, 8, 13, 5, 6, 20, 0], 245.69547889216892),
    ([0, 18, 17, 16, 7, 11, 0], 159.69951465643132),
    ([0, 14, 21, 19, 15, 10, 0], 132.13514967209545),
    ([0, 3, 1, 2, 9, 12, 0], 130.33534969725577)
]

tours = [item[0] for item in tours_and_costs]
calculated_costs = [item[1] for item in tours_and_costs]

# Check if the solution is correct
print(verify_solution(cities, tours, calculated_costs))