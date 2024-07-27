import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(cities, tour, reported_cost):
    if len(cities) != 15:
        return "FAIL"
    
    if not all([tour[0] == tour[-1] == 0]):
        return "FAIL"
    
    if len(tour) != 5:
        return "FAIL"

    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [
    (9, 93),   # City 0 - Depot
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
    (4, 39)    # City 14
]

# Tour solution provided
tour = [0, 1, 10, 8, 0]
reported_cost = 90.54

# Validate the tour
result = validate_tour(cities, tour, reported_show_cost)
print(result)