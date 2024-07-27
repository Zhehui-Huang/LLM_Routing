import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour_and_cost(tour, expected_cost, coordinates):
    # Check the starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except for depot city 0
    visited = set(tour)
    if len(visited) != 10 or any(city not in visited for city in range(10)):
        return "FAIL"
    
    # Calculate the travel cost and compare it with expected cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities' coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Test data
tour = [0, 9, 4, 8, 3, 2, 1, 6, 7, 5, 0]
total_travel_cost = 272.89014796697063

# Validation check
result = validate_tour_and_cost(tour, total_travel_cost, coordinates)
print(result)  # This should output "CORRECT" if all checks pass, otherwise "FAIL".