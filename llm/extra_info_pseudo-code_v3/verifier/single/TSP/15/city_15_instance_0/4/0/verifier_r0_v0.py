import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_and_cost(cities, tour, reported_cost):
    N = len(cities)
    if len(tour) != N + 1:
        return "FAIL"
        
    # Verify if tour starts and ends at the depot:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # Check if all cities except depot are visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != N - 1 or visited != set(range(1, N)):
        return "FAIL"
    
    # Verify the total travel cost
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates
city_coordinates = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Given tour and travel cost
tour = [0, 2, 6, 5, 3, 13, 7, 4, 9, 11, 12, 14, 1, 10, 8, 0]
reported_cost = 339.25546983499316

# Check if the provided tour and cost satisfy the requirements
result = verify_tour_and_cost(city_coordinates, tour, reported_cost)
print(result)