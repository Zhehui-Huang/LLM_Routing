import numpy as np

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Distance calculation
def euclidean_distance(city1, city2):
    return np.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Number of robots
num_robots = 8

# Assign cities to robots using a simple cluster method
# Ignoring city 0 initially as it is the depot
remaining_cities = list(cities.keys())[1:]
np.random.shuffle(remaining_cities)
assigned_cities = np.array_split(remaining_cities, num_robots)

# 2-opt optimization for each robot's tour
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # No need to swap if they are consecutive
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(euclidean_distance(new_route[k], new_route[k + 1]) for k in range(len(new_route) - 1)) < sum(euclidean_distance(best[k], best[k + 1]) for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Determine tours and costs
total_cost = 0
results = []

for i in range(num_robots):
    tour = [0] + list(assigned_cities[i]) + [0]  # Start and end at the depot
    optimized_tour = two_opt(tour)
    cost = sum(euclidean_distance(optimized_tour[j], optimized_tour[j + 1]) for j in range(len(optimized_tour) - 1))
    results.append((i, optimized_tour, cost))
    total_cost += cost

# Output results
for (robot, tour, cost) in results:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")