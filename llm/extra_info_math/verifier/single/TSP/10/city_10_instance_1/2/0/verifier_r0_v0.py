import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, city_coordinates, reported_cost):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    unique_cities_visited = set(tour[1:-1])  # Excludes the first and last city (depot city)
    if len(unique_cities_visited) != len(city_coordinates) - 1:
        return "FAIL"
    
    # Check if tour costs are calculated correctly with Euclidean distance and match the reported cost
    calculated_cost = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        calculated_cost += euclidean_distance(city_coordinates[from_city], city_coordinates[to_city])
    
    if abs(calculated_cost - reported_cost) > 1e-6:  # Precision tolerance
        return "FAIL"
    
    return "CORRECT"

# Defining coordinates of the cities
cities_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Tour given by the solution
reported_tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
reported_cost = 278.9348447394249

# Checking if the solution is correct
test_result = verify_solution(reported_tour, cities_coordinates, reported_cost)
print(test_result)