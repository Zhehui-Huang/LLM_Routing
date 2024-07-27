import math
from itertools import combinations

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
n = len(cities)
distances = [[calc_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Heuristic: Nearest Neighbor starting at the depot
def nearest_neighbor(start, distances):
    tour = [start]
    used = set(tour)
    for _ in range(len(distances) - 1):
        last = tour[-1]
        next_city = min((dist for dist in enumerate(distances[last]) if dist[0] not in used), key=lambda x: x[1])
        tour.append(next_city[0])
        used.add(next_city[0])
    return tour

# 2-opt swap
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Neighbor cities
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_dist(new_tour) < tour_dist(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

def tour_dist(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Construct initial tour and optimize
initial_tour = nearest_neighbor(0, distances)
initial_tour.append(0)  # Return to the depot
optimized_tour = two_opt(initial_tour)

# Calculate tour metrics
total_travel_cost = tour_dist(optimized_tour)
max_distance = max(distances[optimized_tour[i]][optimized_tour[i + 1]] for i in range(len(optimized_tour) - 1))

# Output
print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)