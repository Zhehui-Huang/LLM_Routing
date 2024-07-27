import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, total_cost, max_distance):
    # Check Requirement 1: Visit each city exactly once and return to depot
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"

    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Travel cost as Euclidean distance
    calculated_cost = 0
    distances = []
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        distances.append(distance)
        calculated_cost += distance
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # Check Requirement 3: Minimize the longest distance between consecutive cities
    calculated_max_distance = max(distances)
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Cities data
cities = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Provided solution
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_cost = 373.61
max_distance = 94.11

# Verify the solution
result = verify_tour(cities, tour, total_cost, max_distance)
print(result)