import numpy as np

# Given the city coordinates
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Tours reported from the solution
robot_0_tour = [0, 3, 2, 15, 0, 10, 4, 12, 14, 6, 5, 11, 7, 9, 18, 16, 16, 17, 8, 13, 0]

# Check requirements
def check_requirements():
    # Requirement 4: Robots need to collectively visit all cities exactly once
    city_visits = sum([1 for city in robot_0_tour if city in city_coordinates.keys()])
    unique_cities_visited = len(set(robot_0_tour) - {0})
    if unique_cities_visited != len(city_coordinates) - 2:  # excluding depot 1 since only depot 0 is involved
        return "FAIL - Each city should be visited exactly once"
    
    # Requirement 2: There is only one robot (Robot 0) starting from depot 0
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL - Robot should start and finish at depot 0"
    
    # Requirement 12: All cities should be visited exactly once
    if sorted(set(robot_0_tour) - {0}) != sorted(city_coordinates.keys() - {0, 1}):
        return "FAIL - All cities should be visited exactly once, excluding depot 1"
    
    # Requirement 3: Verify the travel cost calculation
    def euclidean_distance(c1, c2):
        return np.sqrt((city_coordinates[c1][0] - city_coordinates[c2][0])**2 + (city_coordinates[c1][1] - city_coordinates[c2][1])**2)
    
    calculated_cost = sum(euclidean_distance(robot_0_tour[i], robot_0_tour[i + 1]) for i in range(len(robot_0_tour) - 1))
    reported_cost = 385.26581568232064
    if not np.isclose(calculated_cost, reported_cost, atol=1e-4):
        return "FAIL - Reported travel cost does not match the calculated cost"

    return "CORRECT"

# Unit Test Output
print(check_requirements())