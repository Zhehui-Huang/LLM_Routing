import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, coordinates):
    # [Requirement 1]
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    # Check if all cities are visited exactly once, except the depot (0), which must be visited exactly twice
    from collections import Counter
    city_count = Counter(tour)
    if city_count[0] != 2 or any(count != 1 for city, count in city_count.items() if city != 0):
        return "FAIL"
    
    # [Requirement 3]
    # Check if the goal is achieved: Minimize the longest travel distance between consecutive cities
    max_distance = 35.77708763999664  # as obtained in the objective value
    calculated_distances = []
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        dist = calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_distances.append(dist)
        if dist > max_distance:
            return "FAIL"
    
    if max(calculated_distances) > max_distance:
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities as given in the task
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Tour provided by the solver
tour = [0, 9, 7, 2, 5, 12, 4, 11, 6, 3, 10, 14, 8, 13, 1, 0]

# Verify the solution
result = verify_solution(tour, coordinates)
print(result)