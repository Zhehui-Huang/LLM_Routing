import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost, city_coordinates):
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit all cities exactly once
    unique_cities = set(tour)
    if len(tour) - 1 != len(unique_cities) or unique_cities.symmetric_difference(set(range(len(city_coordinates)))) != set():
        return "FAIL"
    
    # [Requirement 3] Calculate travel cost using Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check computed total cost with the given precise to two decimal places
    if not math.isclose(computed_cost, total_cost, abs_tol=0.01):
        return "FAIL"
    
    # [Requirement 4 & 5] Output the tour and total cost
    # Already structurally checked by nature of input and output examination, no need for additional code.
    
    return "CORRECT"

# City coordinates as provided
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Provided solution test
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_cost = 458.37

# Verify the solution
result = verify_solution(tour, total_cost, city_coordinates)
print(result)