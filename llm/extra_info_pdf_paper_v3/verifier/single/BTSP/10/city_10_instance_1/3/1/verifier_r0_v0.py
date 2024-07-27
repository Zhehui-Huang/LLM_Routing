import math

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Tour provided including indices
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
expected_total_cost = 291.41
expected_max_distance = 56.61

# Verify the tour properties
def verify_tour(tour, cities):
    n = len(cities)

    # Starting and ending at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    if sorted(tour[:-1]) != list(range(n)):
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0

    for i in range(len(tour)-1):
        current_distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += current_distance
        if current_distance > max_distance:
            max_distance = current_distance

    # Check if calculations match
    if round(total_cost, 2) != expected_total_cost or round(max_distance, 2) != expected_max_distance:
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Running the verification
print(verify_tour(tour, cities))