import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours provided in the solution
tours = [
    [0, 0, 1],
    [0, 2, 3],
    [0, 4, 5],
    [0, 6, 7],
    [0, 8, 9],
    [0, 10, 11],
    [0, 12, 13],
    [0, 14, 15]
]

# Check if all cities are visited exactly once
visited_cities = [0 for _ in range(23)]
for tour in tours:
    for city in tour:
        if city != 0:  # Excluding the depot city
            visited_cities[city] += 1

# Calculate the actual tour costs and the total cost
calculated_costs = []
total_calculated_cost = 0
for tour in tours:
    tour_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        tour_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    calculated_costs.append(tour_cost)
    total_calculated_cost += tour_cost

# Verify results
expected_costs = [13.892443989449804, 36.320854582406994, 57.827743125481554, 22.041594578792296,
                  49.213016093416115, 39.409727284423084, 54.17408500136381, 77.82812560836184]
reported_total_cost = 181.52352436345896
verification_results = all(city == 1 for city in visited_cities) and len(visited_cities) == 23

# Compare costs with a tolerance for floating point comparison
cost_comparison = all(abs(ec - cc) < 1e-4 for ec, cc in zip(expected_costs, calculateducalculated_costs))
total_cost_comparison = abs(sum(expected_costs) - reported_total_cost) < 1e-4

if verification_results and cost_comparison and total_cost_comparison:
    print("CORRECT")
else:
    print("FAIL")