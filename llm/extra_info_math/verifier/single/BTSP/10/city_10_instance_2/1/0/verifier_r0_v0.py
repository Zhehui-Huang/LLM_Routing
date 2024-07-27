import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tour, city_coordinates):
    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"
    
    # Check if every city in the coordinate list is visited
    if set(tour) != set(range(len(city_coordinates))):
        return "FAIL"

    # Calculate total travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Outputs from CBC solver
    reported_total_travel_cost = 438.1909170192786
    reported_max_distance = 69.42621983083913

    # Check reported total travel cost and longest travel distance
    if not math.isclose(total_travel_global, reported_total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, reported_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities
city_coordinates = [
    (90, 3),  # Depot city
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Solution tour from the solver
solution_tour = [0, 5, 6, 7, 2, 9, 1, 4, 3, 8, 0]

# Verify the solution
verification_result = verify_solution(solution_tour, city_coordinates)
print(verification_result)