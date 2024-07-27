def test_solution(robots_tours, max_travel_cost):
    all_cities_visited = set()
    unique_cities_visited = True
    
    # Test Requirement 1 & 2: Tour starting and ending at depot, and visiting all cities exactly once
    for tour, cost in robots_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            print(f"FAIL: Robot {tour} does not start and end at the depot.")
            return "FAIL"
        all_cities_visited.update(tour)

    # Exclude the depot city and check if all cities from 1 to 22 have been visited
    all_cities_visited.discard(0)
    if all_cities_visited != set(range(1, 23)):
        print("FAIL: Not all cities are visited exactly once.")
        return "FAIL"
    
    # Test Requirement 3: Check if any robot's travel exceeds maximum travel cost reported
    calculated_max_travel_cost = max(cost for tour, cost in robots_tours.items())
    if calculated_max_travel_cost != max_travel_cost:
        print(f"FAIL: Calculated max travel cost {calculated_max_travel_cost} does not match provided {max_travel_cost}.")
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Given example solution details
robots_tours = {
    (0, 4, 15, 19, 9, 13, 2, 0): 121.55,
    (0, 10, 0): 41.62,
    (0, 21, 20, 7, 22, 14, 17, 18, 8, 1, 0): 119.48,
    (0, 0): 0.00,
    (0, 0): 0.00,
    (0, 11, 12, 3, 5, 6, 16, 0): 113.89,
    (0, 0): 0.00,
    (0, 0): 0.00
}

max_travel_cost = 121.55

# Run the unit test
test_result = test_solution(robots_tours, max_travel_cost)
print(test_result)