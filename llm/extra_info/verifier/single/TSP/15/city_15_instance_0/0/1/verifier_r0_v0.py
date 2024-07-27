import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, distances, expected_cost):
    # Requirement 1: The robot must start and end its tour at the depot city, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit all cities exactly once, except for the depot city
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(tour) - 2 or len(visited_cities) != 14:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if any(tour.count(city) > 1 for city in visited_cities):
        return "FAIL"
    
    # Requirement 3: Calculate and check total travel cost
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39),   # City 14
]

# Calculate distances between all cities
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Proposed tour and expected cost
tour = [0, 8, 10, 1, 11, 14, 12, 4, 9, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost = 359.53718629646994

# Verify the solution
result = verify_tour(tour, distances, total_travel_cost)
print(result)