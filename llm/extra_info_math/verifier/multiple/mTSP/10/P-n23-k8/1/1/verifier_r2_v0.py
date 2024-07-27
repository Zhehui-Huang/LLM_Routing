import math

# Define the city coordinates and the solution result for verification
city_coordinates = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
robot_tours = [
    [0, 20, 0],
    [0, 4, 0],
    [0, 10, 0],
    [0, 21, 0],
    [0, 2, 0],
    [0, 16, 0],
    [0, 1, 0],
    [0, 6, 0]
]

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(robot_tours, city_coordinates):
    number_of_cities = len(city_coordinates) - 1  # Exclude the depot
    visited_cities = set()

    for tour in robot_tours:
        # Check for correct start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Add cities to the set (exclude depot from checking)
        for city in tour[1:-1]:
            visited_cities.add(city)

    # Check if all cities are visited exactly once
    if len(visited_cities) != number_of_cities:
        return "FAIL"

    # Check for total distance minimization in provided solution
    reported_cost = 235.67331696088496
    calculated_cost = sum(
        calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        for tour in robot_tours
        for i in range(len(tour) - 1)
    )

    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Run the unit tests to verify the solution
result = verify_solution(robot_tours, city_coordinates)
print(result)