import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_positions, city_groups):
    # Ensure the route starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each city group is visited
    visited_groups = {i: 0 for i in range(len(city_groups))}
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_groups[group_index] += 1

    if any(count != 1 for count in visited_groups.values()):
        return "FAIL"

    # Calculate the actual travel cost to verify it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])

    # Compare the provided travel cost with the calculated cost
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Predefined city positions and groupings
city_positions = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
city_groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

# Solution provided
tour = [8, 3, 0, 0]
total_travel_cost = 253.95833194968426

# Output verification
result = verify_solution(tour, total_travel_cost, city_positions, city_groups)
print(result)