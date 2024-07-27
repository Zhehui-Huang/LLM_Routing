import math
import random

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Coordinates of cities with city index being the key
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8

# Initial assignment of cities to robots
tours = [[] for _ in range(num_robots)]
city_indices = list(cities.keys())[1:]  # exclude the depot city from the indices
random.shuffle(city_indices)  # Shuffle to randomize the initial assignment

robot_index = 0
for city in city_indices:
    tours[robot_index].append(city)
    robotize a tour
    robot_index = (robot_index + 1) % num_robots

# Add depot at the beginning and end of all tours
for tour in tours:
    tour.insert(0, 0)
    tour.append(0)

# Compute total distance for a tour
def compute_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Implement 2-opt optimization to refine tours
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if compute_tour_cost(new_tour) < compute_tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Optimize all tours using 2-opt
optimized_tours = [two_opt(tour) for tour in tours]
tour_costs = [compute_tour_cost(tour) for tour in optimized_tours]
max_cost = max(tour_costs)

# Output the result
for i, tour in enumerate(optimized_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")