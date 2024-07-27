import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities, expected_cost):
    # Checking start and end at depot city, which is city index 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once except the depot city
    visited = set(tour)
    if len(visited) != len(cities) or set(range(len(cities))) != visited:
        return "FAIL"
    
    # Calculate the total travel distance in the provided tour
    total_distance = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        total_distance += calculate_distance(cities[city_index1], cities[city_index2])
    
    # Verify if the calculated distance matches expected cost within a small error margin due to float operations
    if not math.isclose(total_distance, expected_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Define the cities coordinates
cities_coordinates = [
    (53, 68),
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

# The provided tour and expected cost
tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
expected_cost = 290.8376577906224

# Perform the verification
result = verify_tour(tour, cities_coordinates, expected_cost)
print(result)