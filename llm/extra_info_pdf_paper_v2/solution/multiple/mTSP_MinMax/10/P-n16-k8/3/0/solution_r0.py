import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8

# Calculate Euclidean distances between all pairs of cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all pairs distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Greedy initial solution: Split cities into `num_robots` clusters 
# Ideally, better clustering techniques like K-Means or other heuristic partitioning should be used.
cities_per_robot = len(cities) // num_robots
tours = {}
remaining_cities = list(cities.keys())[1:]  # excluding the depot city

for r in range(num_robots):
    if r == num_robots - 1:
        assigned_cities = remaining_cities
    else:
        assigned_cities = remaining_cities[:cities_per_robot]
    remaining_cities = remaining_cities[cities_per_robot:]
    
    # Start and end at the depot
    tour = [0] + assigned_cities + [0]
    tours[r] = tour

# Improve the solution: rudimentary local search (2-opt)
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # skip consecutive cities
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(distances[(new_route[k], new_route[k + 1])] for k in range(len(new_route) - 1)) < \
                   sum(distances[(best[k], best[k + 1])] for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Apply local search to each tour
optimized_tours = {}
for r in tours:
    optimized_tours[r] = two_opt(tours[r])

# Calculate and print the costs
max_cost = 0
for r in optimized_tours:
    tour = optimized_tours[r]
    cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    max_cost = max(cost, max_cost)
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {cost}")

print("Maximum Travel Cost:", max_cost)