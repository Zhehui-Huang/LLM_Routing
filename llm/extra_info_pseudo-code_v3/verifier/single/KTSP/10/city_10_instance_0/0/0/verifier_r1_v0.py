import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution(tour, cost):
    # Cities coordinates
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Check if exactly four cities are visited
    if len(tour) != 5:
        return "FAIL"
    
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check for duplicate cities in the tour (excluding the start and end city)
    if len(set(tour[1:-1])) != 3:
        return "FAIL"
    
    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_index_current = tour[i]
        city_index_next = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city_index_current], cities[city_index_next])
    
    # Check if the calculated cost matches the provided cost
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
provided_tour = [0, 4, 9, 5, 0]
provided_cost = 64.37320494629213

# Testing the solution
result = test_solution(provided_tour, provided_cost)
print(result)