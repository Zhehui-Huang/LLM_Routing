import math

def euclidean_distance(x1, y1, x2, y2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour, coordinates):
    """ Calculate the total travel cost for a single tour based on city coordinates. """
    total_cost = 0.0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return round(total_cost, 2)

def verify_tours_and_costs(tours, total_costs, coordinates):
    """ Verify if the solution meets all the requirements. """
    cities_visited = set()
    all_cities = set(range(1, 16))

    calculated_total_cost = 0
    for robot_id, tour in enumerate(tours):
        # Check if tours start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check each robot's local total cost
        local_cost = calculate_tour_cost(tour, coordinates)
        if not math.isclose(local_cost, total_costs[robot_id], abs_tol=0.01):
            return "FAIL"

        # Accumulate total cost
        calculated_total_cost += local_cost

        # Add cities visited (excluding depot)
        for city in tour[1:-1]:
            cities_visited.add(city)

    # Check if all cities have been visited exactly once
    if cities_visited != all_class:
        return "FAIL"

    # Check the overall total cost
    if not math.isclose(calculated_totalsock, sum(total_costs), abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Given coordinates of cities including the depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Robot tours as provided
tours = [
    [0, 1, 9, 0],
    [0, 10, 2, 0],
    [0, 11, 3, 0],
    [0, 4, 12, 0],
    [0, 5, 13, 0],
    [0, 6, 14, 0],
    [0, 7, 15, 0],
    [0, 8, 0]
]

# Total costs for each robot as provided
total_costs = [72.88, 52.46, 86.04, 64.99, 68.36, 64.17, 83.62, 64.90]
overall_total_cost_provided = 557.42

# Verification
result = verify_tours_and_costs(tours, total_costs, coordinates)
print(result)  # Output the result which should be either "CORRECT" or "FAIL"