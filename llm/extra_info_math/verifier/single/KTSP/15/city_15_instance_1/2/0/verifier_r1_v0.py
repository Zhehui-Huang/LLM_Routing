import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(cities, tour, total_cost):
    # Validate the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Validate exactly 6 cities visited
    if len(tour) != 7:  # Includes the depot twice (start and end)
        return "FAIL"
    
    # Calculate the travel cost and ensure all cities are visited once
    calculated_cost = 0
    visited = set()
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        visited.add(city_from)
        calculated_cost += euclidean_distance(cities[city_from], cities[city_to])
    
    # Check if all cities in the tour (except depot repeated) are visited exactly once
    if len(visited) != 6 or 0 not in visited:
        return "FAIL"
    
    # Check calculated cost matches reported total cost within floating point tolerance
    if not math.isclose(calculated_cost, total_listed_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# The position of each city
# city_index: (x_position, y_position)
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Solution tour and its total cost
solution_tour = [0, 6, 1, 7, 3, 9, 0]
total_listed_cost = 118.8954868377263

print(validate_tour(cities, solution_tour, total_listed_cost))