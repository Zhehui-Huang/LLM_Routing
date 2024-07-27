import math
import random

# Constants and data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]
num_robots = 8
depots = [0]

# Helper functions
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(tour):
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = random.randint(1, len(tour) - 2)
        j = random.randint(1, len(tour) - 2)
        if i != j:
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            old_cost = total_distance(tour)
            new_cost = total_distance(new_tour)
            if new_cost < old_cost or random.random() < math.exp((old_cost - new_cost) / T):
                tour = new_tour
        T *= alpha
    return tour

# Split cities between robots, starting at depot
cities = list(range(1, 16))  # Exclude depot (0)
random.shuffle(cities)  # Randomize city order
chunk_size = len(cities) // num_robots
chunks = [cities[i:i + chunk_size] for i in range(0, len(cities), chunk_size)]

# Generate and optimize tours for each robot
tours = []
for i in range(num_robots):
    chunk = chunks[i % len(chunks)] if i < len(chunks) else []
    tour = [0] + chunk  # Start at depot city (0)
    optimized_tour = simulated_annealing(tour)
    tours.append(optimized_tour)

# Calculate and print results
total_overall_cost = 0
for i, tour in enumerate(tours):
    cost = total_distance(tour)
    total_overall_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_overall_cost, 2)}")