import random
import math
from itertools import permutations

# Coordinates of the 22 cities including depot at index 0
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Number of robots
num_robots = 4

# Generate an initial feasible solution by assigning cities to the closest tour
def initial_solution():
    cities = list(range(1, len(coordinates)))   # ignore depot at 0
    random.shuffle(cities)  # Random shuffle for initial distribution
    tours = [list() for _ in range(num_robots)]
    for i, city in enumerate(cities):
        tours[i % num_robots].append(city)
    return tours

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = euclidean_distance(0, tour[0])  # from depot to first city
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    cost += euclidean_distance(tour[-1], 0)  # from last city to depot
    return cost

# Simple shake: relocate a random city from one tour to another tour
def shake(tours, k):
    for _ in range(k):
        src_tour_id = random.randrange(len(tours))
        if len(tours[src_tour_id]) == 0:
            continue
        city = tours[src_tour_id].pop(random.randrange(len(tours[src_tour_id])))
        dest_tour_id = random.randrange(len(tours))
        tours[dest_tour_id].append(city)

# Local search procedure: optimize tour by performing 2-opt swaps
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                if euclidean_distance(tour[i - 1], tour[j]) + euclidean_distance(tour[i], tour[j + 1]) < euclidean_distance(tour[i - 1], tour[i]) + euclidean_distance(tour[j], tour[j + 1]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True

# Main GVNS function
def gvns(tmax=30):
    tours = initial_solution()
    max_time = tmax
    start_time = time.time()

    while time.time() - start_time < max_time:
        k = 1
        while k < 5:
            new_tours = [list(t) for t in tours]
            shake(new_tours, k)
            for tour in new_tours:
                two_opt(tour)
            new_costs = [calculate_tour_cost(tour) for tour in new_tours]
            old_costs = [calculate_tour_cost(tour) for tour in tours]
            if max(new_costs) < max(old_costs):
                tours = new_tours
                k = 1
            else:
                k += 1

    return tours

# Run the algorithm and format output
tours = gvns()
for i, tour in enumerate(tours):
    total_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {[0] + tour + [0]}")
    print(f"Robot {i} Total Travel Cost: {total_cost}")

max_cost = max(calculate_tour_cost(tour) for tour in tours)
print(f"Maximum Travel Cost: {max_cost}")