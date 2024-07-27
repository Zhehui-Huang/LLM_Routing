import math

# Coordinates of cities
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Given solution
tour = [0, 19, 8, 10, 15, 4, 3, 6, 17, 18, 13, 11, 14, 2, 5, 16, 7, 12, 9, 1, 0]
reported_total_cost = 489.06
reported_max_distance = 56.52

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_tour(tour):
    n = len(cities)
    total_traveled_distance = 0.0
    max_distance = 0.0
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour contains exactly all cities once (excluding the repeated depot city at the end)
    if sorted(tour[:-1]) != list(range(n)):
        return "FAIL"

    # Calculate the total travel cost and the maximum distance between consecutive cities
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i + 1])
        total_traveled_distance += distance
        if distance > max_distance:
            max_distance = distance

    # Verify the calculations with the reported values
    if not math.isclose(total_traveled_distance, reported_total_cost, rel_tol=1e-3):
        return "FAIL"
    if not math.isclose(max_distance, reported_max_distance, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_tour(tour)
print(result)