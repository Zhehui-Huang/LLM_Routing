import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, reported_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except depot city which is visited twice
    unique_cities = set(tour)
    if len(tour) - 1 != len(cities) or unique_cities != set(range(len(cities))):
        return "FAIL"

    # Calculate the total travel cost and compare with the reported cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Solution provided in the prompt
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
reported_total_cost = 294.17253892411236

# Perform verification using the corrected function
result = verify_solution(cities, tour, reported_total_cost)
print(result)