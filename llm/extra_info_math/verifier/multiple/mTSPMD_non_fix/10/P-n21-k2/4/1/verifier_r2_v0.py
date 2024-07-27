def verify_solution(tours, costs, coordinates):
    # Requirement 1: Robots must collectively visit all cities exactly once.
    all_visited_cities = set()
    for tour in tours:
        # Check for unique visit in a single tour
        if len(set(tour)) != len(tour):
            return "FAIL"
        all_visited_cities.update(tour)
    
    # Check for all cities visited exactly once
    if sorted(all_visited_cities) != list(range(len(coordinates))):
        return "FAIL"

    # Requirement 2: Each robot starts from a designated depot
    depots = [0, 1]  # Depots as per problem statement
    for i, tour in enumerate(tours):
        if tour[0] != depots[i % len(depots)]:  # Robots start from depots cyclically
            return "FAIL"

    # Requirement 3 & 4: Minimize and optimize the total travel cost
    # Calculating the costs manually to verify
    def euclidean_distance(p1, p2):
        from math import sqrt
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    calculated_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(1, len(tour)):
            city_from = tour[i - 1]
            city_to = tour[i]
            tour_cost += euclidean_distance(coordinates[city_from], coordinates[city_to])
        calculated_costs.append(tour_cost)
    
    if not all(abs(cost - calc_cost) < 1e-5 for cost, calc_cost in zip(costs, calculated_costs)):
        return "FAIL"
    
    return "CORRECT"

# Defining the cities coordinates based on the previously provided data
coordinates = [
    (30, 40), (37, 52),
    (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Tours and costs provided by the CBC MILP Solver Solution
tours = [
    [0, 16],
    [1, 10, 4, 11, 15, 12, 3, 19, 18, 8, 2, 7, 13, 9, 17, 14, 5, 20, 6]
]

tour_costs = [
    0,
    145.64571836122954
]

# Check for the correctness of the solution
solution_status = verify_solution(tours, tour_costs, coordinates)
print(solution_status)