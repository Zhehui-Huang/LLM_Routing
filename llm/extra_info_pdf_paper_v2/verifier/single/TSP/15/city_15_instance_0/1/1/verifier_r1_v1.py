import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(cities, tour, reported_cost):
    # Verify start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that each city is visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    # Verify all cities are visited
    if unique_cities != set(range(1, len(cities))):
        return "FAIL"
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i+1]]
        total_cost += euclidean_distance(city_a[0], city_a[1], city_b[0], city_b[1])

    # Compare calculated cost with reported cost
    if not math.isclose(total_cost, reported_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (9, 93),  # Depot city 0
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

# Provided solution
tour = [0, 8, 10, 1, 11, 14, 12, 4, 9, 7, 3, 5, 6, 2, 13, 0]
reported_cost = 359.54

# Check if the solution is correct
result = verify_tour(cities, tour, reported_macost)
print(result)