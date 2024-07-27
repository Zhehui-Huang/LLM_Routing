def verify_solution(tours):
    # Initialize city count only for cities from 1 to 15
    cities_count = {i: 0 for i in range(1, 16)}
    total_cities_visited = 0

    for robot_tour in tours:
        # Check if each tour starts and ends at the depot
        if robot_tour[0] != 0 or robot_tour[-1] != 0:
            return "FAIL"

        # Check each tour does not visit the depot in between or handle cities incorrectly
        previous_city = robot_tour[0]
        for city in robot_tour[1:-1]:  # Only inspect inside the tour (not including starting/ending depot)
            if city == 0:
                # Fails if depot is visited in between the tour
                return "FAIL"
            if city in cities_count:
                cities_count[city] += 1
            previous_city = city
        
        # Calculate total visited cities (excluding depot stops)
        total_cities_visited += len(set(robot_tour) - {0})

    # Verify each city is visited exactly once
    if any(count != 1 for count in cities_count.values()):
        return "FAIL"

    # Verify the total cities visited match 15 (total unique cities to visit)
    if total_cities_visited != 15:
        return "FAIL"

    return "CORRECT"

# Provided tours from the MILP solution
robot_tours = [
    [0, 11, 15, 0],
    [0, 10, 0],
    [0, 5, 0],
    [0, 2, 9, 12, 0],
    [0, 6, 0],
    [0, 7, 0],
    [0, 1, 8, 0],
    [0, 4, 3, 13, 14, 0]
]

# Validate the solution
print(verify_solution(robot_tours))