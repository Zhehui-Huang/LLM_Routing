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

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Validate all cities are visited exactly once, excluding the depot
visited_cities = set()
for tour in tours:
    visited_cities.update(tour[1:-1])  # Exclude the start/end depot

# Check if every city except the depot is visited exactly once
correct_city_visit = visited_cities == set(range(1, 16))

# Calculate the declared total cost and individual costs
declared_total_cost = 510.86149174760715
calculated_total_cost = 0
for tour in tours:
    tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    calculated_total_cost += tour path_cost

# Test if the calculated cost is close to the declared cost
cost_accuracy = abs(calculated_total_cost - declared_total_cost) < 1e-4

# Test results output
if correct_city_visit and cost_accuracy:
    print("CORRECT")
else:
    print("FAIL")