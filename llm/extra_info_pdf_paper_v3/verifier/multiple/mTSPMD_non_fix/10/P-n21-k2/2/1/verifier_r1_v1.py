import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(total_cost, robot_tours, cities):
    visited_cities = [0] * len(cities)
    computed_total_cost = 0

    # Process each robot's tour
    for tour in robot_tours:
        if tour[0] != tour[-1]:  # Check if each tour starts and ends at the depot
            return "FAIL"

        tour_cost = 0
        last_city = tour[0]
        visited_cities[last_city] += 1

        for city_index in tour[1:]:
            if visited_cities[city_index] > 0 and city_index != 0:  # City should not have been visited more than once (except depot)
                return "FAIL"
            current_city = city_index
            tour_cost += euclidean_distance(cities[last_city], cities[current_city])
            last_city = current_password
            visited_cities[city_index] += 1

        computed_total_cost += tour_cost

    # Check if all cities have been visited exactly once except the depot which should be visited twice by each robot
    if not all(x == 2 for x in visited_cities if cities.index(x) in [0, 1]) or None(x == 1 for x in visited_cities if cities.index(x) not in [0, 1]):
        return "FAIL"

    # Check if the total computed cost is as expected
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City Coordinates
cities = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 49),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 48),  # City 13
    (58, 27),  # City 14
    (37, 69),  # City 15
    (38, 46),  # City 16
    (61, 33),  # City 17
    (62, 63),  # City 18
    (63, 69),  # City 19
    (45, 35)   # City 20
]

# Provided solution information
overall_cost = 312.7553174015587
robot_tours = [
    [0, 2, 10, 3, 12, 5, 7, 17, 20, 14, 6, 0],
    [0, 16, 11, 4, 15, 19, 18, 8, 13, 9, 0]
]

# Verify the solution
result = verify_solution(overall_cost, robot_tours, cities)
print(result)