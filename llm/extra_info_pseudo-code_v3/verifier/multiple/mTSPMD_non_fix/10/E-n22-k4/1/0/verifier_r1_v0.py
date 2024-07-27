import math

# Helper function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities with coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Provided solution
solution_tours = [
    [0, 14, 17, 20, 10, 5, 4],
    [0, 16, 19, 21, 9, 2],
    [0, 12, 15, 18, 7, 1],
    [0, 13, 11, 8, 6, 3]
]

solution_costs = [137.51, 127.28, 111.48, 75.14]
calculated_costs = []

def verify_solution():
    # Check if all cities are visited exactly once
    all_cities = set(range(22))
    visited_cities = {city for tour in solution_tours for city in tour}
    if visited_cities != all_cities:
        return "FAIL"
    
    # Compute tours' costs and verify against provided costs
    overall_cost = 0
    for tour, reported_cost in zip(solution_tours, solution_costs):
        tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        calculated_costs.append(round(tour_cost, 2))
        overall_cost += tour_cost
        if round(tour_cost, 2) != reported_cost:
            return "FAIL"

    # Verify overall costs
    if round(overall_cost, 2) != 451.40:
        return "FAIL"
    
    return "CORRECT"

# Run the verification function
result = verify_solution()
print(result)