import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, claimed_total_cost, claimed_max_distance):
    n = len(cities)
    visited = [False] * n

    # Check if tour starts and ends at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check all cities are visited exactly once, except the depot city 0
    visited_count = [0] * n
    for idx in tour:
        visited_count[idx] += 1
    if visited_count[0] != 2 or any(count != 1 for i, count in enumerate(visited_count) if i != 0):
        return "FAIL"

    # Calculate the actual travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check claimed total cost and maximum distance
    if not (math.isclose(total_cost, claimed_total_cost, rel_tol=1e-5) and
            math.isclose(max_distance, claimed_max_distance, rel_tol=1e-5)):
        return "FAIL"

    return "CORRECT"

# Coordinates of city positions
cities = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Provided solution
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_travel_cost = 373.61498801130097
max_distance = 94.11163583744573

# Run verification
result = verify_tour(cities, tour, total_travel_cost, max_distance)
print(result)