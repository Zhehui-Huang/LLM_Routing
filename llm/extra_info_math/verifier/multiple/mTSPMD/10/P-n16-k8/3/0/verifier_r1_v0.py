def test_solution(robot_tours, expected_total_cost):
    assigned_depots = list(range(8))  # As per robot information provided earlier
    
    # Check if each robot starts and ends at its assigned depot
    for robot_id, tour in enumerate(robot_tours):
        if tour[0] != assigned_depots[robot_id] or tour[-1] != assigned_depots[robot_id]:
            return "FAIL"

    # Check if all cities are visited exactly once collectively
    visited_cities = set()
    for tour in robot_tours:
        visited_cities.update(tour[1:-1])  # Exclude start/end depot in the counting

    all_cities = set(range(16))  # Total 16 cities
    if visited_cities != all_cities:
        return "FAIL"
    
    # Calculate total cost of all tours
    total_cost = sum([
        173.01,  # Robot 0 Total Travel Cost
        183.6,   # Robot 1 Total Travel Cost
        168.67,  # Robot 2 Total Travel Cost
        198.97,  # Robot 3 Total Travel Cost
        170.18,  # Robot 4 Total Travel Cost
        194.02,  # Robot 5 Total Travel Cost
        173.01,  # Robot 6 Total Travel Cost
        175.56   # Robot 7 Total Travel Cost
    ])
    
    # Check if the calculated total cost matches the expected total cost
    if abs(total_cost - expected_total_cost) > 0.01:  # Tolerating small floating point arithmetic errors
        return "FAIL"

    return "CORRECT"

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

expected_total_cost = 1437.02

# Print the result of the test
print(test_solution(robot_tours, expected_total_cost))