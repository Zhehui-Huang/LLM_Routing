import numpy as np

# Define the cities and their coordinates
cities = {
    0: (26, 60), # depot
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

# Provided solution
tour = [0, 3, 15, 9, 12, 7, 5, 6, 4, 16, 14, 8, 11, 1, 18, 19, 0]
travel_cost_provided = 544.0856463642627

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour_and_cost(tour, provided_cost):
    # Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly 16 cities including the depot
    if len(set(tour)) != 16:
        return "FAIL"

    # Requirement 5: Tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total travel cost using Euclidean distance
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += calculate_euclidean_distance(tour[i], tour[i + 1])

    # Requirement 6: Check provided cost
    if not np.isclose(total_travel_cost, provided_cost, atol=0.01):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Conduct the verification
result = verify_tour_and_cost(tour, travel_cost_provided)
print(result)