import math

# Assigning the solution tours and costs provided to variables
tours = {
    0: ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14, 0], 236.07),
    1: ([1, 16, 6, 20, 5, 22, 7, 2, 13, 9, 17, 14, 21, 0, 10, 12, 15, 4, 11, 3, 8, 18, 19, 1], 240.19),
    2: ([2, 7, 22, 5, 20, 6, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 21, 0, 2], 228.95),
    3: ([3, 8, 18, 19, 12, 15, 4, 11, 10, 1, 16, 6, 20, 5, 22, 7, 2, 13, 9, 17, 14, 21, 0, 3], 231.28),
    4: ([4, 11, 15, 12, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 16, 1, 10, 2, 7, 17, 14, 21, 0, 4], 220.67),
    5: ([5, 22, 7, 2, 13, 9, 17, 14, 20, 6, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 21, 0, 5], 240.97),
    6: ([6, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 7, 2, 21, 0, 14, 17, 6], 246.11),
    7: ([7, 22, 5, 20, 6, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 2, 21, 0, 7], 236.26)
}

coordinates = {
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

# Calculating Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Check if solution is correct
def verify_solution(tours):
    all_visited_cities = set()
    overall_cost = 0
    
    for robot_id, (tour, reported_cost) in tours.items():
        if tour[0] != robot_id or tour[-1] != robot_id:  # Requirement 1
            return "FAIL"

        # Requirement 2 (Unique city visit across tours)
        cities_in_tour = set(tour[1:-1])  # excluding starting/ending depot
        if any(city in all_visited_cities for city in cities_in_tour):
            return "FAIL"
        all_visited_cities.update(cities_in_tour)

        # Computing total travel cost
        calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):  # Requirement 3
            return "FAIL"
        
        overall_cost += reported_cost
    
    if len(all_visited_cities) != 22:  # 23 cities including depots, check if all 22 are visited exactly once
        return "FAIL"
    
    return "CORRECT"  # If all checks are passed

# Running the unit test
print(verify_solution(tours))