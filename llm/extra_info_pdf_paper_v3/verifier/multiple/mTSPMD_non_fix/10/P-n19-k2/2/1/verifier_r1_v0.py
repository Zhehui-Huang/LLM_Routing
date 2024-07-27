import math

# Helper function to calculate Euclidean distance between two cities.
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Define city coordinates as provided in the task description.
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Test the solution
def test_solution(tours, costs):
    all_cities = set(range(19))
    visited_cities = set()
    total_calculated_costs = []

    for i, tour in enumerate(tours):
        # Checking the starting point requirement
        if tour[0] != i:
            return "FAIL"

        # Check if no city is revisited within a tour and collect cities
        if len(set(tour)) != len(tour):
            return "FAIL"

        visited_cities.update(tour)
        
        # Check travel cost accuracy and starting-ending at depot
        tour_cost = 0
        for j in range(len(tour) - 1):
            tour_cost += euclidean_distance(cities[tour[j]], cities[tour[j+1]])
        total_calculated_costs.append(tour_cost)
        
        # Adding the cost from the last city back to the depot (if needed)
        if tour[-1] != i:
            tour_cost += euclidean_distance(cities[tour[-1]], cities[i])
            total_calculated_costs[-1] = tour_cost
        
        # Verify individual tour costs with provided data
        if not math.isclose(tour_cost, costs[i], abs_tol=1e-6):
            return "FAIL"

    # Check if all cities are visited
    if visited_cities != all_cities:
        return "FAIL"

    # Check if the total travel cost is minimized (or just the provided total is calculated correctly)
    if not math.isclose(sum(costs), sum(total_calculated_costs), abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Example usage of the testing function:
tours = [
    [0, 8, 13, 12, 2, 6, 18, 11, 16, 0],
    [1, 3, 4, 14, 5, 15, 17, 9, 10, 7, 1]
]

costs = [257.2664049280195, 223.06700270802438]

# Check if the solution is correct based on the provided tours and costs
result = test_solution(tours, costs)
print(result)  # Expected output should be "CORRECT" if all checks are met correctly.