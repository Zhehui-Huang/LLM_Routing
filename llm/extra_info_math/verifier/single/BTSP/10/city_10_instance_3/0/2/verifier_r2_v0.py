def verify_solution(tour, distances):
    # [Requirement 1] The robot must start and end the tour at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once by the robot.
    visited_cities = set(tour)
    all_cities = set(range(len(distances)))
    if visited_cities != all_cities:
        return "FAIL"

    # [Requirement 3] Minimize the longest distance between any two consecutive cities in the tour.
    max_distance = 68.26419266350405  # from solver output
    computed_max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if abs(computed_max_distance - max_distance) > 1e-6:
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Compute distances between all cities
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solution from the solver
tour = [0, 4, 7, 6, 5, 9, 3, 8, 2, 1, 0]

# Verify the solution
result = verify_solution(tour, distances)
print(result)