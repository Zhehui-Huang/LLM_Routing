def check_solution(robot_tours, n_cities):
    visited_cities = set()
    depot_visits = 0

    # Requirement 2: Validate if tours start and end at depot and collect all visited cities
    for tour in robot_tours:
        start_city, end_city = tour[0], tour[-1]
        if start_city != 0 or end_city != 0:
            return "FAIL"
        
        depot_visits += 2
        visited_cities.update(tour)

    # Remove the depot and count visits
    visited_cities.discard(0)

    # Requirement 1: Each city visited exactly once and only non-depot cities included
    if len(visited_cities) != n_cities - 1 or len(visited_cities) != max(visited_cities):
        return "FAIL"

    return "CORRECT"

# Provided solution
robot_tours = [
    [0, 2, 13, 9, 8, 0],
    [0, 15, 12, 3, 0],
    [0, 21, 6, 0],
    [0, 14, 17, 0],
    [0, 16, 1, 10, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 20, 5, 22, 7, 0]
]

n_cities = 23  # 23 cities indexed from 0 to 22

# Execute the check
result = check_solution(robot_tours, n_cities)
print(result)