import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35)
}

def calculate_dist(city1, city2):
    """ Calculates the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def verify_solution(tour, expected_cost):
    if tour[0] != tour[-1]:  # Check requirement 1: Start and End at depot
        return "FAIL"
    
    visited = set()
    total_cost = 0

    for i in range(1, len(tour)):
        current_city = tour[i]
        previous_city = tour[i-1]

        if current_city < 0 or current_city > 20:
            return "FAIL"  # Invalid city number

        if current_city in visited and current_city not in [0, 1]:  # Check requirement 2
            return "FAIL"
        visited.add(current_city)

        # Calculate travel cost (Requirement 3)
        total_cost += calculate_dist(previous_city, current_city)

    # Check if all cities are visited, considering required visits at depot which do not count as duplicates
    if len(visited) != 20 or (0 not in visited or 1 not in visited):
        return "FAIL"

    # Check the total cost (Requirement 4)
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Example tour provided for checking
tour = [0, 2, 2, 6, 20, 20, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 3, 10, 1]
expected_cost = 92.38960849433072 
result = verify_solution(tour, expected_cost)
print(result)