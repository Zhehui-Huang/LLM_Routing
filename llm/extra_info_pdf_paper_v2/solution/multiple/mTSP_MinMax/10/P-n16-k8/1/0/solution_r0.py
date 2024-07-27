import math
import random

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Initialization of cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8

# Greedy initial solution - each robot is assigned cities one by one
tours = [[] for _ in range(num_robots)]
city_indices = list(cities.keys())[1:]  # exclude the depot city from the indices
random.shuffle(city_indices)

robot_index = 0
for city in city_calls:
    tours[robot_index].append(city)
    robot_index = (robot_index + 1) % num_robots

# Insert depot to the start and end of each tour
for tour in tours:
    tour.insert(0, 0)
    tour.append(0)

# Function to compute total tour cost
def compute_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Function to perform 2-opt swap
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        best_cost = compute_tour_cost(best)
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]
                new_cost = compute_tour_cost(new_tour)
                if new_cost < best_cost:
                    best = new_tour
                    best_cost = new_cost
                    improved = True
        tour = best
    return tour

# Optimize each tour with 2-opt
optimized_tours = [two_opt(tour) for tour in tours]
tour_costs = [compute_tour_cost(tour) for tour in optimized_tours]
max_cost = max(tour_costs)

# Output the results
for i, tour in enumerate(optimized_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")