import math

# City coordinates including the Depot as the first entry
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Provided solution
tour = [0, 6, 2, 12, 5, 10, 9, 3, 13, 7, 4, 11, 1, 14, 8, 0]
total_travel_cost = 375.55332674488494
maximum_distance_between_consecutive_cities = 39.051248

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, expected_total_cost, expected_max_distance):
    # Requirement 1: Starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    if len(set(tour)) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Calculate actual costs and distances
    calculated_cost = 0
    calculated_max_distance = 0
    
    previous_city = tour[0]
    for city in tour[1:]:
        distance = euclidean_distance(cities[previous_city], cities[city])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
        previous_city = city
        
    # Requirement 3 and 4: Minimize max distance and validate distances
    if not (math.isclose(calculated_cost, expected_total_cost, rel_tol=1e-5) and
            math.isclose(calculated_max_distance, expected_max_distance, rel_tol=1e-5)):
        return "FAIL"
    
    return "CORRECT"

# Use the verify_solution function to perform the unit test
result = verify_solution(tour, cities, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)