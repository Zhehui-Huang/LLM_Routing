import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tsp_solution(tour, total_cost, coordinates):
    # Verify tour starts and ends at the depot (Requirement 1 and 5)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify each city except the depot is visited exactly once (Requirement 2)
    visited_cities = set(tour)
    if len(visited_cities) != len(coordinates) or any(tour.count(city) != 1 for city in range(1, len(coordinates))):
        return "FAIL"
    
    # Check that the computed cost is correct (Requirements 3 and 4)
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass, return "CORRECT"
    return "CORRECT"

# Coordinates of the cities including the depot
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided tour and total cost
tour = [0, 19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
total_cost = 398.667866225166

# Verify the tour and total cost
result = verify_tsp_solution(tour, total_cost, coordinates)
print(result)