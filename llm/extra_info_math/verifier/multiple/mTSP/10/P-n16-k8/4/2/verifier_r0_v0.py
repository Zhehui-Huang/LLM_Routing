def verify_solution(tours):
    cities_count = {i: 0 for i in range(1, 16)}
    total_cities_visited = 0

    for robot_tour in tours:
        # Check if each tour starts and ends at the depot
        if robot_tour[0] != 0 or robot_tour[-1] != 0:
            return "FAIL"

        # Check for subtours within each robot tour
        visited_in_tour = set()
        for i in range(1, len(robot_tour) - 1):
            city = robot_tour[i]
            if city in visited_in_tour:
                return "FAIL"
            visited_in_tour.add(city)
            cities_count[city] += 1
        
        # Verify continuous path without skipping back to the depot illegally
        for i in range(1, len(robot_tour) - 1):
            if robot_tour[i] == 0 and i not in (0, len(robot_tour) - 1):
                return "FAIL"

        total_cities_visited += len(visited_in_tour)

    # Verify each city is visited exactly once
    for count in cities_count.values():
        if count != 1:
            return "FAIL"

    # Verify the total cities visited match expected, excluding the depot
    if total_cities_visited != 15:
        return "FAIL"

    return "CORRECT"

# Provided tours from the MILP solution
robot_tours = [
    [0, 11, 0, 15, 0],
    [0, 10, 0, 0],
    [0, 5, 0, 0],
    [0, 2, 0, 9, 12, 0],
    [0, 6, 0, 0],
    [0, 7, 0, 0],
    [0, 1, 0, 8, 0],
    [0, 4, 3, 0, 13, 14, 0]
]

# Validate the solution
print(verify_solution(robot_tours))