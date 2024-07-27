def check_solution(tour, total_travel_cost, group_details):
    # Requirement 1: The robot needs to visit exactly one city from each group of cities.
    visited_groups = set()
    for city in tour:
        for group_id, cities in enumerate(group_details):
            if city in cities:
                visited_groups.add(group_id)
    
    if len(visited_groups) != len(group_details):
        return "FAIL"
    
    # Requirement 2: The robot must start and end its tour at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Define city positions
    city_positions = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Measure the total travel distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        from_city, to_city = tour[i], tour[i + 1]
        from_pos, to_pos = city_positions[from_city], city_positions[to_city]
        distance = ((from_pos[0] - to_pos[0]) ** 2 + (from_pos[1] - to_pos[1]) ** 2) ** 0.5
        calculated_cost += distance

    # Requirement 3: Calculated cost must be very close to given total travel cost to verify accuracy.
    # Check with a small tolerance for floating-point precision issues.
    if abs(calculated_cost - total_travel_flow) > 1e-3:
        return "FAIL"
    
    return "CORRECT"

# Given details
group_details = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

# Solution to be tested
tour = [0, 8, 0]
total_travel_cost = 8.246211251235321

# Execute test
test_result = check_solution(tour, total_travel_cost, group_details)
print(test_score)