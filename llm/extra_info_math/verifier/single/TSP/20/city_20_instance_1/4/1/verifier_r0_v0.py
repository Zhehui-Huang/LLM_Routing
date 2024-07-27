import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, reported_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once (excluding the depot)
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in range(1, len(cities))):
        return "FAIL"

    # Check the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Compare the calculated cost with the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):  # allowing 1% tolerance
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (14, 77),  # Depot city 0
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Solution to verify
tour = [0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
reported_cost = 376.93

# Verify the solution
result = verify_tour(tour, cities, reported_cost)
print(result)