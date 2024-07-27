import math

def calculate_euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_cost, cities_coordinates):
    """Validate the tour based on the requirements."""
    
    # Requirement 1: Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if exactly 7 cities are visited
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Requirement 3 Check if total travel cost is correct
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(
            cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 5: Validate the format of the tour (implicit by input, could add more checks if needed)

    # If all checks pass, the solution is correct
    return "CORRECT"

# City coordinates from the provided problem statement
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), 
    (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided solution
tour = [0, 14, 4, 16, 18, 9, 6, 0, 0]
total_cost = 215.07

# Validate the solution
result = validate_solution(tour, total_cost, city_coordinates)
print(result)