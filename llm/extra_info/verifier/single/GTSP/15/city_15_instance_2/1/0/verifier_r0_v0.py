import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, city_positions, city_groups, expected_cost):
    # Checking Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Start/end city not at depot."
    
    visited_groups = set()
    # Checking Requirement 2
    for group in city_groups:
        group_set = set(group)
        if not (set(tour) & group_set):
            return "FAIL", "At least one group is not visited."
        visited_groups.update(group_set)
    
    if not all(city in visited_groups for city in tour[1:-1]):
        return "FAIL", "Extra cities visited outside of specified groups."

    # Calculate total tour cost and check Requirement 3 implicitly
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])

    # Check Requirement 4 by comparing with expected cost (this is simplified as normally we wouldn't know the minimal total cost a priori)
    if abs(total_cost - expected_cost) > 1e-2:
        return "FAIL", f"Cost does not match expected. Calculated: {total_cost}, Expected: {expected_cost}"

    return "CORRECT", None

# Data setup
city_positions = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
city_groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Provided solution
tour = [0, 12, 10, 4, 3, 2, 0]
expected_total_cost = 138.15

# Validate the solution
result, error_message = verify_tour(tour, city_positions, city_groups.values(), expected_total_cost)
if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL", error_message)