import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Demands of the cities
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15,
    8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# Number of robots and their capacities
num_robots = 8
robot_capacity = 35

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate initial savings list (i.e., savings by combining two cities in one trip)
savings = []
for i in range(1, len(cities)):
    for j in range(i + 1, len(cities)):
        if i != j:
            s_ij = distance(0, i) + distance(0, j) - distance(i, j)
            savings.append((s_ij, i, j))
savings.sort(reverse=True, key=lambda x: x[0])  # Sort savings in descending order

# Assign routes to robots using a probabilistic mechanism
routes = [[] for _ in range(num_robots)]
remaining_capacity = [robot_capacity] * num_robots
assigned = set()

def can_assign_route(route, city):
    if city in assigned or demands[city] > remaining_capacity[routes.index(route)]:
        return False
    return True

for _, i, j in savings:
    for route in routes:
        if can_assign_route(route, i) and can_assign_route(route, j):
            route.extend([i, j])
            assigned.update([i, j])
            remaining_capacity[routes.index(route)] -= (demands[i] + demands[j])
            break

# Post-improvement procedure: trying to swap and reassign to optimize the routes
# Attempting to refine routes by swapping nodes if it leads to lower costs without violating constraints
for k in range(50):  # Number of iterations for local optimization
    for route in routes:
        random.shuffle(route)
        for i in range(len(route)):
            for j in range(i + 1, len(route)):
                route[i], route[j] = route[j], route[i]  # Swap two cities
                # Check if the swap is beneficial
                if sum(distance(route[x], route[x + 1]) for x in range(len(route) - 1)) <= sum(distance(route[x], route[x - 1]) for x in range(1, len(route))):
                    continue
                else:
                    route[i], route[j] = route[j], route[i]  # Swap back if not beneficial

# Compose final routes and calculate costs
overall_cost = 0
for ind, route in enumerate(routes):
    tour = [0] + route + [0]
    cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    overall_cost += cost
    print(f"Robot {ind} Tour: {tour}")
    print(f"Robot {ind} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")