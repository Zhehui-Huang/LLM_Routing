import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits exactly one city from each group
    visited_cities_from_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_cities_from_groups:
                    return "FAIL"
                visited_cities_from_groups.add(group_index)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    # Check if the robot visited one city from each group
    if len(visited_cities_from_groups) != len(city_groups):
        return "FAIL"
    
    # Check the total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = city_coordinates[city1]
        x2, y2 = city_coordinates[city2]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if abs(calculated_cost - total_cost) > 1e-2:
        return "FAIL"

    return "CORRECT"

# City coordinates and groups based on the task
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

city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Provided tour and total cost
tour = [0, 8, 11, 6, 2, 0]
total_cost = 103.12

# Running the verification
result = verify_solution(tour, total_cost, city_coordinates, city_groups)
print(result)