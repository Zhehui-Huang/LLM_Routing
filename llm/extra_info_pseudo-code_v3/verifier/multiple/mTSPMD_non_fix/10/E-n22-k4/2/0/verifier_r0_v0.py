import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1], coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
    return round(total_cost, 2)

def verify_solution(tours, expected_costs, coordinates, expected_total_cost):
    # Check if each city is visited exactly once
    visited_cities = set()
    for tour in tours:
        visited_cities.update(tour)
    
    if len(visited_cities) != len(coordinates):
        return "FAIL: Not all cities are visited or some are visited more than once."

    # Check if the total travel cost for each tour is correct
    calculated_costs = []
    for tour in tours:
        cost = calculate_travel_cost(tour, coordinates)
        calculated_costs.append(cost)
    
    for idx, cost in enumerate(expected_costs):
        if abs(cost - calculated_costs[idx]) > 1e-2:  # Allowing for minor floating-point discrepancies
            return f"FAIL: Travel cost mismatch for robot {idx}. Expected: {cost}, Found: {calculated_costs[idx]}"

    # Check overall cost
    if abs(sum(calculated_costs) - expected_total_cost) > 1e-2:
        return f"FAIL: Overall travel cost mismatch. Expected: {expected_total_cost}, Found: {sum(calculated_costs)}"

    # Check if each tour starts and ends at the correct depot (all start from 0 and end at 0 in this configuration)
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the correct depot."

    return "CORRECT"

# City coordinates
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Robot tours and their corresponding costs
tours = [
    [0, 14, 13, 6, 7, 9, 0],
    [0, 15, 18, 17, 5, 4, 0],
    [0, 11, 8, 19, 21, 20, 0],
    [0, 16, 12, 10, 0]
]

# Expected costs for each tour
expected_costs = [110.84, 184.64, 151.24, 62.71]

# Expected total cost
expected_total_cost = 509.44

# Verify the solution
print(verify_solution(tours, expected_costs, coordinates, expected_total_cost))