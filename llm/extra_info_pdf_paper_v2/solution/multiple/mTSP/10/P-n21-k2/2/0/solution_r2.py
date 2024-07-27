import numpy as np
import math
import random

# City coordinates (excluding depot city 0)
coordinates = [
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Depot city coordinates
depot = (30, 40)

# Euclidean distance calculation
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate cost of a given tour
def calculate_tour_cost(tour, coordinates_with_depot):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates_with_depot[tour[i]], coordinates_with_depot[tour[i + 1]])
    return cost

def simulated_annealing(tour, coordinates_with_depot, temp=1000, cooling_rate=0.003, steps=1000):
    current_cost = calculate_tour_cost(tour, coordinates_with_depot)
    while temp > 1:
        for _ in range(steps):
            new_tour = tour[:]
            i, j = sorted(random.sample(range(1, len(tour) - 1), 2))  # Exclude the depot
            # Reverse the segment between i and j
            new_tour[i:j+1] = new_tour[i:j+1][::-1]
            new_cost = calculate_tour_cost(new_tour, coordinates_with_depot)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                tour, current_cost = new_tour, new_cost
        temp *= (1 - cooling_rate)
    return tour, current_cost

# Fixed splitting strategy for simplicity
split_index = len(coordinates) // 2
robots_tours = {
    0: [0] + list(range(1, split_index + 1)) + [0],
    1: [0] + list(range(split_pos + 1, len(coordinates) + 1)) + [0]
}

# Include depot in coordinates for easy indexing
coordinates_with_depot = [depot] + coordinates

# Optimize each robot's tour using simulated annealing and calculate total costs
optimized_tours = {}
total_cost = 0
for robot, tour in robots_tours.items():
    optimized_tour, tour_cost = simulated_annealing(tour, coordinates_with_depot)
    optimized_tours[robot] = (optimized_tour, tour_cost)
    total_cost += tour_cost
    print(f"Robot {robot} Tour: {optimized_tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")