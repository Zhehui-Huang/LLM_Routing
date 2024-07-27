import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_solution(tour, total_cost):
    # Coordinates of the cities
    coordinates = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits each city exactly once (excluding the depot city)
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != 14 or any(city not in visited_cities for city in range(1, 15)):
        return "FAIL"
    
    # Calculate the total travel cost and compare with the provided total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Allowing a small floating point tolerance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 4, 10, 9, 3, 7, 1, 6, 14, 8, 2, 12, 11, 13, 5, 0]
total_cost = 355.52

# Validate the provided solution
result = validate_solution(tour, total_cost)
print(result)