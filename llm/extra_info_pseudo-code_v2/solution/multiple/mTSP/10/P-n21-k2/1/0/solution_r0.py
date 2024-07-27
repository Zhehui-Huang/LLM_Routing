import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def nearest_neighbor_tour(start, cities, distances):
    unvisited = set(cities)
    current = start
    tour = [current]
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)  # return to depot
    return tour

def two_opt(tour, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # consecutive edges; no need to check
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(new_tour, distances) < calculate_total_distance(tour, distances):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate distances between all cities
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Number of robots
num_robots = 2

# Assign cities to robots; simple division 
cities_per_robot = len(coordinates[1:]) // num_robots
assignments = [list(range(1, cities_per_robot + 1)), list(range(cities_per_robot + 1, len(coordinates)))]

# Construct tours using nearest neighbor and then optimize with 2-opt
tours = []
total_costs = []

for i in range(num_robots):
    tour = nearest_neighbor_tour(0, assignments[i], distances)
    optimized_tour = two_opt(tour, distances)
    tours.append(optimized_tour)
    total_costs.append(calculate_total_distance(optimized_tour, distances))

# Output results
overall_cost = sum(total_costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")