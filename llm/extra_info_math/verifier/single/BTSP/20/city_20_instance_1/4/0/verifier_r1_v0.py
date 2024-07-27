def verify_solution(tour, total_cost, max_distance):
    # Given information about cities and their coordinates
    coordinates = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
        6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
        12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
        18: (50, 28), 19: (69, 9)
    }

    # Requirement 1: The robot must start and end its journey at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city must be visited exactly once by the robot.
    visited = set(tour[1:-1])  # Exclude the first and last since it's depot city
    if len(visited) != len(coordinates) - 1:  # Subtract 1 because city 0 is the depot and shouldn't be double counted
        return "FAIL"

    # Calculate the total travel distance and max distance between consecutive cities
    def euclidean_distance(city1, city2):
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    calculated_total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i + 1])
        calculated_total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check if calculated values match given values, considering a float comparison tolerance
    tolerance = 1e-5
    if abs(calculated_total_distance - total_cost) > tolerance or abs(calculated_max_distance - max_distance) > tolerance:
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Data from provided solution output
tour = [0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0]
total_travel_cost = 1255.3883861180173
maximum_distance = 62.76941930590086

# Verify the solution
solution_status = verify_solution(tour, total_travelorast, mssistance)
print(solution_status)