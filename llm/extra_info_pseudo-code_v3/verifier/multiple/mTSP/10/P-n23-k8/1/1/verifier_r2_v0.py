import math

# Cities and Coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Robot tours as provided in the solution
robot_tours = [
    [0, 2, 8, 13, 9, 0],
    [0, 3, 12, 15, 0],
    [0, 6, 21, 0],
    [0, 14, 17, 0],
    [0, 1, 10, 16, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 7, 22, 5, 20, 0]
]

# Distance calculation using the Euclidean formula
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Validate that each city is visited exactly once and calculate total distances
all_cities_visited = set()
total_computed_cost = 0

for tour in robot_tours:
    # Validate correct start and end
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        break

    # Calculate tour cost
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += calculate_distance(tour[i], tour[i + 1])

    # Add cities from this tour to the set, skipping the depot city
    all_cities_visited.update(tour[1:-1])
    total_computed_cost += tour_value

# Check that all cities except depot are visited and check for precision mismatch
if (len(all_cities_visited) == 22 and abs(total_computed_cost - 500.34) < 1e-2):
    print("CORRECT")
else:
    print("FAIL")