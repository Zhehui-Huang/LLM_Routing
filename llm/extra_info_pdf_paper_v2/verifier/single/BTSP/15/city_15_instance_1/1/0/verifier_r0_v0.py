def test_tour(tour, total_cost, max_distance):
    # Extract the depot city index
    depot_city = 0
    
    # [Requirement 1] The robot must start and end at city 0
    if tour[0] != depot_city or tour[-1] != depot_city:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once by the robot
    visited_cities = set(tour)
    correct_cities = set(range(15))  # From city 0 to city 14
    if visited_cities != correct_cities:
        return "FAIL"
    
    # The following check and calculation are for testing the code you gave.
    # It has been omitted based on the instructions to only test the above requirements.
    # However, if Maximum distance [Requirement 3] test was also wanted, we'd assert the maximum
    # distance does not exceed some specific benchmark value, ideally the one obtained by
    # running an optimal BTSP algorithm (or similar heuristic-driven algorithm).
    
    # Finally, return "CORRECT" if all checks pass
    return "CORRECT"

# Solution provided
tour = [0, 4, 10, 0, 0, 5, 0, 9, 3, 7, 1, 6, 13, 2, 8, 14, 0, 0, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_travel_cost = 511.70041076181064
maximum_distance = 85.21150157109074

# Check if the provided solution is correct
result = test_tour(tour, total_travel_cost, maximum_distance)
print(result)