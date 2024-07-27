def test_robot_tour():
    # Given tour and travel cost
    tour = [0, 5, 0, 7, 6, 0, 0]
    total_travel_cost = 77.22145135944956
    
    # Coordinates of cities
    coordinates = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # City groups
    city_groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }

    # Check Requirement 1: Start and end at depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Exactly one city from each group
    visited_cities = tour[1:-1]  # ignore start and end depot in checks
    unique_group_visits = set()
    for city in visited_cities:
        for group_id, cities in city_groups.items():
            if city in cities:
                unique_group_visits.add(group_id)
    if len(unique_group_visits) != len(city_groups):
        return "FAIL"

    # Compute the actual total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += ((coordinates[city_to][0] - coordinates[city_from][0]) ** 2 +
                            (coordinates[city_to][1] - coordinates[city_from][1]) ** 2) ** 0.5

    # Check Requirement 3: Shortest possible distance
    if not abs(calculated_cost - total_travel_cost) < 1e-5:  # Allow small floating-point tolerance
        return "FAIL"

    return "CORRECT"

# Run the unit test to verify the solution
result = test_robot_tour()
print(result)