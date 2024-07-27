import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, city_coordinates, expected_total_cost):
    """Verify if the solution meets all the requirements."""
    # [Requirement 1] Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 7 cities are visited
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate total travel cost and compare with expected
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # [Requirement 3] Check the total cost with a small margin due to float operations
    if not math.isclose(total_cost, expected_total_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Given solution
solution_tour = [0, 4, 1, 7, 3, 8, 0]
solution_cost = 128.73

# Verify the solution
result = verify_tour(solution_tour, cities, solution_cost)
print(result)