import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tour, proposed_cost, city_coordinates):
    num_cities = len(city_coordinates)

    # Requirement: Verify the robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: Verify the robot visits exactly 8 cities
    if len(tour) != 9:
        return "FAIL"
    
    # Preparing to check the tour validity and cost calculation
    current_cost = 0
    visited_cities = set()

    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        
        # Check if cities are within valid range
        if city_from >= num_cities or city_to >= num_cities:
            return "FAIL"
        
        # Calculate segment cost
        current_cost += calculate_euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])
        
        # Collect visited cities excluding the depot city if visited multiple times
        if city_from != 0 or (city_from == 0 and len(visited_cities) == 0):
            visited_cities.add(city_from)

    # Check if all cities are unique except the return to depot city
    if len(visited_cities) != 8:
        return "FAIL"
    
    # Requirement: Check if the computed cost matches the proposed cost within a small error margin to account for float comparison
    if not math.isclose(current_cost, proposed_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Coordinates for the 10 cities including the depot
city_coordinates = [
    (79, 15), # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Given tour solution and the proposed cost
given_tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
proposed_cost = 235.38

# Perform verification
result = verify_solution(given_tour, proposed_cost, city_coordinates)
print(result)