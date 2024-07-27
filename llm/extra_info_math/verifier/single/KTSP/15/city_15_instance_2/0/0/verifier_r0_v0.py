import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tour, total_cost, city_coordinates):
    # Check requirement 1: start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2: visit exactly 8 cities (unique) including city 0
    if len(set(tour)) != 8 or len(tour) != 9:
        return "FAIL"
    
    # Check requirement 3: Calculate the total length of the tour and check with given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i + 1]
        x1, y1 = city_coordinates[city_1]
        x2, y2 = city_coordinates[city_2]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
city_coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Given solution to check
tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
total_travel_cost = 132.1185774560832

# Run the check
result = check_solution(tour, total_travel_stat_cost, city_coordinates)
print(result)