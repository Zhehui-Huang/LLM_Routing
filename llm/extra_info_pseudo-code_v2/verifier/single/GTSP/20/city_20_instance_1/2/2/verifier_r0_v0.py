import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, city_coordinates, city_groups):
    if tour is None:
        return "FAIL"

    # Check if tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # ignore the starting and ending depot city
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(group_index)
                break
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check if the travel cost in the tour matches the total_travel_cost provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if abs(calculated_cost - total_travel_cost) > 0.01:  # allow a small numerical tolerance
        return "FAIL"
    
    return "CORRECT"

# Example city coordinates and groups setup based on the task description
city_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Provided solution
tour = [0, 17, 16, 19, 3, 0]
total_travel_cost = 290.49

# Verify solution
result = verify_solution(tour, total_travel_cost, city_coordinates, city_groups)
print(result)