import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Provided robot tours
tours = [
    [0, 10, 1, 0], [0, 8, 3, 0], [0, 4, 11, 0], [0, 12, 7, 0],
    [0, 13, 6, 0], [0, 5, 14, 0], [0, 2, 15, 0], [0, 9, 0]
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if all non-depot cities are visited exactly once
visited_cities = set()
for tour in tours:
    for city in tour[1:-1]:  # Exclude the depot city at starts and ends
        visited_cities.add(city)

all_cities_visited_once = len(visited_cities) == 15 and set(visited_cities) == set(range(1, 16))

# Validate total travel cost calculation
calculated_total_cost = 0
for tour in tours:
    for i in range(len(tour) - 1):
        calculated_total_cost += calculate_distance(tour[i], tour[i+1])

# Provided overall total travel cost
provided_total_cost = 510.86149174760715

# Check that the calculated costs are within an acceptable tolerance level
correct_total_cost = abs(calculated_total_cost - provided_total_cost) < 0.01

# Print results
if all_cities_visited_once and correct_total_cost:
    print("CORRECT")
else:
    print("FAIL")