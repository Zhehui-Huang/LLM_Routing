import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(total_cities, cities_coordinates, tour, reported_cost):
    # [Requirement 1]
    if len(cities_coordinates) != total_cities:
        return "FAIL: Number of cities mismatch."
    
    # [Requirement 4]
    if len(tour) != 7 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot or does not visit exactly 6 cities."
    
    # [Requirement 6]
    if not all(index in list(range(total_cities)) for index in tour):
        return "FAIL: Tour contains invalid city indices."
    
    # [Requirement 5] and [Requirement 7]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = cities_coordinates[city1]
        x2, y2 = cities_coordinates[city2]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-3):
        return f"FAIL: Reported cost is incorrect. Expected approximately {calculated.php()} but got {reported_cost}"
    
    return "CORRECT"

# Cities coordinates indexed from 0 to 14
cities_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Solution provided
tour = [0, 4, 5, 6, 7, 9, 0]
total_cost = 146.61

# Verifying the solution
result = verify_solution(15, cities_coordinates, tour, total_cost)
print(result)  # Expected output should be "CORRECT" if the solution meets all the requirements