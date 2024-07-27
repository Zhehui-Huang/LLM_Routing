import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_and_cost(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at the depot city 0.
    
    if len(set(tour)) != len(cities):
        return "FAIL"  # The robot must visit all cities exactly once.

    # Check the travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city1], cities[city2])
    
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.001):
        return "FAIL"  # Costs should match up to a reasonable precision.

    return "CORRECT"

# City coordinates: city index is the list index
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), 
          (22, 21), (97, 70), (20, 99), (66, 62)]

# Given solution for evaluation
tour = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_travel_cost = 328.58208011724435

# Validate the provided tour and travel cost
result = verify_tour_and_cost(tour, total_travel_cost, cities)
print(result)