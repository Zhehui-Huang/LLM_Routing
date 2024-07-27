import math

# Cities and Coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Robot tours as provided in the solution
robot_tours = [
    [0, 2, 8, 13, 9, 0],
    [0, 3, 12, 15, 0],
    [0, 6, 21, 0],
    [0, 14, 17, 0],
    [0, 1, 10, 16, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 7, 22, 5, 20, 0]
]

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Validate the solution
def validate_solution():
    all_cities_visited = set()
    total_computed_cost = 0
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i + 1])
        
        all_cities_visited.update(tour[1:-1])
        total_computed_cost += tour_cost

    if len(all_cities_visited) != 22:
        return "FAIL"
   
    expected_cost = 500.34
    if abs(total_computed_cost - expected_cost) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Output the result
print(validate_solution())