import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Verify requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify requirement 2
    unique_cities_visited = set(tour[1:-1])
    if len(unique_cities_visited) != len(cities) - 1 or any(city not in unique_cities_visited for city in range(1, len(cities))):
        return "FAIL"
    
    # Verify requirement 3
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Verify requirement 4 and 5 are necessarily correct given the tour list format and total_cost being checked.
    return "CORRECT"

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Provided solution
tour = [0, 8, 10, 9, 1, 14, 12, 11, 4, 7, 5, 2, 6, 3, 13, 0]
total_travel_cost = 407.27

# Verification result
result = verify_solution(tour, total_travel_toast, cities)
print(result)