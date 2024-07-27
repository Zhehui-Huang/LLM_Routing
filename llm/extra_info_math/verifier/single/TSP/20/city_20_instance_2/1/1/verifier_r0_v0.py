import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, total_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities from 1 to 19 are visited exactly once
    visited_cities = set(tour[1:-1])  # Exclude the depot city in the start and end
    if len(visited_cities) != 19 or any(city not in visited_cities for city in range(1, 20)):
        return "FAIL"
    
    # Compute the actual travel cost and compare
    computed_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Solution details
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 9, 2, 5, 1, 17, 4, 3, 10, 8, 6, 0]
total_travel_cost = 431.16959178265

# Check if the solution is correct
result = verify_tour(cities, tour, total_travel_cost)
print(result)