import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, cities, total_cost, max_distance):
    # Requirement 1: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city is visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(tour.count(city) > 1 for city in tour if city != 0):
        return "FAIL"
    
    # Calculate the actual total cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Requirement 3: Calculated values should match with given total_cost and max_distance
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9) or not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city positions
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12),
          (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Solution provided
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.570870788815
maximum_distance_between_cities = 85.21150157109074

# Validate solution
result = validate_solution(tour, cities, total_travel_cost, maximum_distance_between_cities)
print(result)