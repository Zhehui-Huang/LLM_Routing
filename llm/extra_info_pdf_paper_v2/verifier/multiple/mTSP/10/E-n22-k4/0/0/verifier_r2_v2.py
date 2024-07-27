import math

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(cities, tours, calculated_costs):
    # Verify that each robot starts and ends at the depot
    if not all(tour[0] == 0 and tour[-1] == 0 for tour in tours):
        return "FAIL"

    # Verify that all cities except the depot are visited exactly once
    visited_cities = [city for tour in tours for city in tour[1:-1]]
    if set(visited_cities) != set(range(1, 22)):
        return "FAIL"
    
    # Verify if the sum of the computed distances for each tour matches the provided distances
    total_computed_cost = 0
    for tour, reported_cost in zip(tours, calculated_costs):
        computed_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            computed_cost += calculate_euclidean_distance(cities[city1], cities[city2])
        if not math.isclose(computed_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"
        total_computed_cost += computed_cost

    # Verify if the sum of the computed cost matches the overall provided cost
    reported_total_cost = sum(calculated_costs)
    if not math.isclose(total_computed_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Define city coordinates: index: (x, y)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Tours and their reported costs
tours_and_costs = [
    ([0, 4, 8, 13, 5, 6, 20, 0], 245.69547889216892),
    ([0, 18, 17, 16, 7, 11, 0], 159.69951465643132),
    ([0, 14, 21, 19, 15, 10, 0], 132.13514967209545),
    ([0, 3, 1, 2, 9, 12, 0], 130.33534969725577)
]

# Perform verification
verification_result = verify_solution(cities, [tour[0] for tour in tours_and_costs], [cost[1] for cost in tours_and_costs])
print(verification_result)