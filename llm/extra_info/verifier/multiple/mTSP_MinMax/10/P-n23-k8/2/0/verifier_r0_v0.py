import math

# Helper function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Tours provided by the solution
tours = [
    [0, 2, 8, 9, 13, 0],
    [0, 3, 12, 15, 0],
    [0, 6, 21, 0],
    [0, 14, 17, 0],
    [0, 1, 10, 16, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 5, 7, 20, 22, 0]
]

# Validate each requirement

# Check if all and only the cities (except the depot) are visited exactly once
all_cities_visited = set(range(1, 23))
cities_visited = set()

for tour in tours:
    for city in tour:
        if city != 0:
            cities_visited.add(city)

# Checking tours to make sure they all start and end at the depot, city 0
all_start_end_at_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# Check if all tours include valid cities between 0 and 22
valid_city_indices = all(all(0 <= city <= 22 for city in tour) for tour in tours)

# Verify calculated distances with the provided distances
tour_calculated_costs = []
for tour in tours:
    cost = sum(euclidean_distance(
        coordinates[tour[i]][0], coordinates[tour[i]][1],
        coordinates[tour[i+1]][0], coordinates[tour[i+1]][1]
    ) for i in range(len(tour) - 1))
    tour_calculated_costs.append(round(cost, 2))

provided_costs = [86.16, 78.2, 24.48, 69.36, 42.67, 89.42, 57.39, 77.66]

# Checking costs within a small tolerance due to rounding
costs_match = all(abs(tour_calculated_costs[i] - provided_costs[i]) < 0.01 for i in range(len(provided_costs)))

# Condition for success in all checks
if (all_cities_visited == cities_visited and all_start_end_at_depot and valid_city_indices and costs_match):
    print("CORRECT")
else:
    print("FAIL")