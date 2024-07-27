def verify_solution(tours, costs):
    # Expected total cost
    expected_total_cost = 1437.07
    
    # Setup helper variables
    visited_cities = set()
    actual_total_cost = sum(costs)
    num_cities = 16
    
    # Verify that each city is visited exactly once and tours start/end at the correct depot
    for i, tour in enumerate(tours):
        if tour[0] != tour[-1] or tour[0] != i:
            return "FAIL"  # Start or end depot is incorrect
        visited_cities.update(tour)
    
    # Check if all cities are visited exactly once (each city should appear only once)
    if len(visited_cities) != num_cities or any(tours.count(city) > 1 for city in visited_cities):
        return "FAIL"

    # Check if the total cost is minimized (should be the expected total cost)
    if not (expected_total_cost - 0.01 <= actual_total_cost <= expected_total_cost + 0.01):
        return "FAIL"

    return "CORRECT"


# Tours and costs provided in the solution:
robot_tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0],
    [1, 10, 12, 15, 4, 11, 3, 8, 13, 9, 7, 5, 14, 6, 2, 0, 1],
    [2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 10, 1, 6, 0, 2],
    [3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 4, 11, 15, 12, 0, 3],
    [4, 11, 15, 12, 3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 0, 4],
    [5, 7, 2, 13, 9, 14, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 5],
    [6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0, 6],
    [7, 5, 14, 9, 13, 2, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 7]
]
robot_costs = [173.01, 183.61, 168.69, 198.97, 170.19, 194.03, 173.01, 175.56]

# Verify the solution:
result = verify_solution(robot_tours, robot_costs)
print(result)