import math

# City coordinates as initially defined
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Provided Robot tours
robot_tours = {
    0: [0, 14, 1, 0],
    1: [0, 12, 4, 0],
    2: [0, 8, 9, 0],
    3: [0, 5, 10, 0],
    4: [0, 13, 11, 0],
    5: [0, 15, 3, 0],
    6: [0, 2, 7, 0],
    7: [0, 6, 0]
}

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to check all requirements
def verify_solution():
    # Check all cities are visited exactly once
    all_visited_cities = [city for tour in robot_tours.values() for city in tour]
    unique_cities = set(all_visited_cities)
    if len(all_visited_cities) != len(unique_cities) or len(unique_cities) != 16:
        return "FAIL: Not all cities are visited exactly once."

    # All tours should start at depot city 0
    if any(tour[0] != 0 for tour in robot_tours.values()):
        return "FAIL: Some tours do not start at depot city 0."

    # Calculate and validate travel costs
    total_calculated_cost = 0
    provided_costs = [
        77.41279750494509, 64.98936367308863, 81.27545517717891, 69.8954448079152,
        94.17242872917295, 78.20189727339391, 51.59051533249141, 24.08318915758459
    ]
    
    for i, tour in enumerate(robot_tours.values()):
        tour_cost = sum(calculate_distance(cities[tour[j]], cities[tour[j + 1]]) for j in range(len(tour) - 1))
        total_calculated_cost += tour_cost
        if not math.isclose(tour_cost, provided_costs[i], abs_tol=1e-5):
            return f"FAIL: Cost mismatch for robot {i}."

    # Verify total cost
    if not math.isclose(total_calculated_cost, 541.6210916557707, abs_tol=1e-5):
        return "FAIL: Total cost mismatch."

    return "CORRECT"

# Execute the verification
result = verify_solution()
print(result)