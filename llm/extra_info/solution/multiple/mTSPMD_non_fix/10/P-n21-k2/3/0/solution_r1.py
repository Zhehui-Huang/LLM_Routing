import math
from itertools import combinations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

depots = {0: 0, 1: 1}
num_robots = 2

# Create a distance matrix
distance_matrix = { (i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j }

# Assign cities to robots
city_assignments = { 0: [], 1: [] }
unassigned_cities = set(cities.keys()) - {0, 1}

for city in sorted(unassigned_cities):  # Simple even distribution of cities
    if len(city_assignments[0]) <= len(city_assignments[1]):
        city_assignments[0].append(city)
    else:
         city_assignments[1].append(city)

# Include depots at start of each robot's tour
robot_tours = { r: [depot] + city_assignments[r] for r, depot in depots.items() }

# Compute tours costs
def tour_cost(tour):
    return sum(distance_matrix[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

tour_costs = { r: tour_cost(tour) for r, tour in robot_tours.items() }
overall_cost = sum(tour_costs.values())

# Print definitive tours and costs
for r in range(num_robots):
    print(f"Robot {r} Tour: {robot_tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_costs[r]}")
print(f"Overall Total Travel Cost: {overall_cost}")