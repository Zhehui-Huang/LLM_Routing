import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, provided_cost):
    cities_coordinates = [
        (90, 3),  # Depot City 0
        (11, 17), # City 1
        (7, 27),  # City 2
        (95, 81), # City 3
        (41, 54), # City 4
        (31, 35), # City 5
        (23, 95), # City 6
        (20, 56), # City 7
        (49, 29), # City 8
        (13, 17)  # City 9
    ]

    city_groups = [
        [3, 6],  # Group 0
        [5, 8],  # Group 1
        [4, 9],  # Group 2
        [1, 7],  # Group 3
        [2]      # Group 4
    ]

    # Check the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Skip first and last as they are the depot
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1

    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(
            cities_coordinates[tour[i]], 
            cities_coordinates[tour[i+1]]
        )

    if abs(calculated_cost - provided_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 3, 5, 2, 1, 9, 0]
total_travel_cost = 273.3072642077373

# Verify the solution
solution_status = verify_solution(tour, total_travel_cost)
print(solution\\.status)