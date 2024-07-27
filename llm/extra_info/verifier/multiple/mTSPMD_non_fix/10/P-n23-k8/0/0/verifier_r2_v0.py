import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def verify_solution(robot_tours, total_costs, overall_total_cost, coordinates):
    all_cities = set(range(23))
    visited_cities = set()
    calculated_overall_cost = 0
    for i, tour in enumerate(robot_tours):
        # Requirement 1: Each tour must start at city 0.
        if tour[0] != 0:
            return "FAIL"

        # Requirement 2: Visit cities exactly once
        visited_cities.update(tour)

        # Requirement 3: Using Euclidean distance
        calculated_cost = calculate_total_cost(tour, coordinates)
        if not math.isclose(calculated_cost, total_costs[i], rel_tol=1e-9):
            return "FAIL"

        calculated_overall_cost += calculated_cost

    # Requirement 2 continued: Each city must be visited exactly once, and tours collectively include all cities.
    if visited_cities != all_cities:
        return "FAIL"

    # Requirement 7: Check total costs
    if not math.isclose(calculated_overall_cost, overall_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

robot_tours = [[0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 0], [0, 7, 8, 0], [0, 9, 10, 0], [0, 11, 12, 0],
               [0, 13, 14, 0], [0, 15, 16, 17, 18, 19, 20, 21, 22, 0]]

individual_costs = [47.28555690793142, 75.67537984747364, 47.93463581488838, 72.1927221713905,
                    77.87109113044761, 74.15812335008223, 80.99113763798833, 217.70164329021412]

overall_cost = 693.8102901504162

# Verify the solution and print result
result = verify_solution(robot_tours, individual_costs, overall_cost, coordinates)
print(result)