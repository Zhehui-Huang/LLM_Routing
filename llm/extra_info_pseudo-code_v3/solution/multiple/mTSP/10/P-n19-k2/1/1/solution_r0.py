import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial clustering (using two cluster centers)
cluster_centers = [cities[0], cities[9]]
assignments = {0: [], 1: []}

for city in cities:
    if city != 0:
        distance_to_cluster1 = distance(0, city)
        distance_to_cluster2 = distance(9, city)
        if distance_to_cluster1 < distance_to_cluster2:
            assignments[0].append(city)
        else:
            assignments[1].append(city)

# Local search optimization (2-opt)
def two_opt_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                if j-i == 1:
                    continue # consecutive edges are not allowed
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if distance(tour[i-1], tour[i]) + distance(tour[j-1], tour[j]) > distance(tour[i-1], tour[j-1]) + distance(tour[i], tour[j]):
                    tour = new_tour
                    improved = True
    return tour

# Generate and optimize tours
tours = {}
total_costs = {}

for robot in assignments:
    # Include depot as start and end
    tour = [0] + assignments[robot] + [0]
    optimized_tour = two_opt_tour(tour)
    tours[robot] = optimized_tour
    total_costs[robot] = sum(distance(optimized_tour[i], optimized_tour[i+1]) for i in range(len(optimized_tour)-1))

# Output results
overall_cost = sum(total_costs.values())
for robot in tours:
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"\nOverall Total Travel Cost: {overall_cost}")