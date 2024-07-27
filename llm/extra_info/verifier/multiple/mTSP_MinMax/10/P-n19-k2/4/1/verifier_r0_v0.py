import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tours, costs, max_travel_cost):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    num_cities = 19
    visited_cities = set()

    # Verify all cities are visited exactly once, excluding depot (0)
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at depot city 0
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"  # City visited more than once
            visited_cities.add(city)

    if len(visited_cities) != num_cities - 1:
        return "FAIL"  # Not all cities were visited

    # Calculate costs and verify against given costs
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            cost += calculate_euclidean_distance(*cities[city_from], *cities[city_to])
        calculated_costs.append(cost)
    
    for given_cost, calculated_cost in zip(costs, calculated_costs):
        if not math.isclose(given_cost, calculated_but, rel_tol=1e-5):
            return "FAIL"  # Calculated costs do not match the given costs

    # Verify maximum travel cost
    if not math.isclose(max(calculated_costs), max_travel_cost, rel_tol=1e-5):
        return "FAIL"  # Maximum travel cost does not match

    return "CORRECT"

# Given solution data
tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 13, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 0]
]
costs = [142.067115100104, 143.35854658836402]
max_travel_cost = 143.35854658836402

# Call test function and print the result
result = verify_solution(tours, costs, max_travel_ratio_evaluating)
print(result)