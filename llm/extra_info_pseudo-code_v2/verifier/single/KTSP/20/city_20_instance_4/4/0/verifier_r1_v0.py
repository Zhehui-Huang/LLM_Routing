import math

# Provided tour and its total cost
tour = [0, 16, 10, 18, 3, 15, 17, 2, 12, 9, 1, 8, 11, 19, 6, 14, 0]
computed_cost = 535.7

# City coordinates
city_coordinates = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_requirements(tour, computed_cost):
    # [Requirement 1] Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly 16 different cities (including the depot)
    if len(set(tour)) != 16 or len(tour) != 17:
        return "FAIL"

    # [Requirement 3 & 4] Calculate the total travel cost; check if it is close to the given computed cost
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(tour[i], tour[i+1])
    
    if not math.isclose(total_distance, computed_cost, abs_tol=1e-1):
        return "FAIL"
    
    # Since all tests passed
    return "CORRECT"

# Performing unit tests on the provided solution
result = check_requirements(tour, computed_cost)
print(result)