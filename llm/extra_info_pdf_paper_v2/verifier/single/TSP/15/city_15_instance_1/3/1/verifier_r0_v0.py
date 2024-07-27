import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost):
    # Coordinates for each city indexed by city number
    coordinates = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once, except the depot city
    unique_cities = set(tour)  # Set of cities in the tour
    if len(unique_cities) != len(coordinates) or len(tour) != len(coordinates) + 1:
        return "FAIL"
    
    # [Requirement 3] Check if the total cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 4 & 5] Are implicitly checked by the logical flow and return statements
    return "CORRECT"

# Provided solution details
tour = [0, 4, 10, 9, 3, 7, 1, 6, 14, 8, 12, 11, 2, 13, 5, 0]
total_travel_cost = 355.8278916013674

# Verify the solution
result = verify_tour(tour, total_travel_cost)
print(result)