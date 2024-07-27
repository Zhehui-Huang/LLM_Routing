import math

# Define the function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities with their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
    4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
    8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Proposed tour, total cost, and max distance
tour = [0, 2, 12, 4, 13, 7, 13, 9, 10, 5, 3, 12, 11, 1, 14, 1, 8, 6, 0]
reported_total_cost = 357.76
reported_max_distance = 31.26

# Check for requirement 1
visited_cities = set(tour)
starts_and_ends_at_depot = tour[0] == 0 and tour[-1] == 0
correct_visitation = len(visited_cities) == len(cities) and all(city in visited_cities for city in cities)

# Check for requirement 2 - Since it's an optimization, we cannot verify optimality but can setup for future testing

# Verify the computational correctness for the total tour cost and maximum distance
computed_total_cost = 0
computed_max_distance = 0

for i in range(1, len(tour)):
    distance = calculate_distance(cities[tour[i-1]], cities[tour[i]])
    computed_total_cost += distance
    computed_max_distance = max(computed_max_distance, distance)

# Check if computed matches reported
matches_cost = math.isclose(computed_total_cost, reported_total_cost, rel_tol=1e-2)
matches_max_distance = math.isclose(computed_max_distance, reported_max_distance, rel_tol=1e-2)

# All conditions check
if starts_and_ends_at_depot and correct_visitation and matches_cost and matches_max_distance:
    print("CORRECT")
else:
    print("FAIL")