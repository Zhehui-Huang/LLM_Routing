import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_tour():
    cities = {
        0: (35, 40),
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }

    tour_proposed = [0, 13, 14, 10, 11, 12, 4, 7, 2, 9, 5, 1, 0]
    proposed_cost = 253.2

    # Requirement 1: Start and end at depot 0
    if tour_proposed[0] != 0 or tour_proposed[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly 12 cities, including the depot
    if len(set(tour_proposed)) != 12 or 0 not in tour_proposed:
        return "FAIL"

    # Requirement 3: Calculate travel costs using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour_proposed)-1):
        city1_index = tour_proposed[i]
        city2_index = tour_proposed[i+1]
        calculated_cost += calculate_distance(cities[city1_index], cities[city2_index])
    calculated_cost = round(calculated_cost, 1)  # Round to match provided cost precision

    # Requirement 4: Check if the calculated cost matches the proposed cost closely
    if abs(calculated_cost - proposed_cost) > 0.1:
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_tour())