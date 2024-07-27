import math
import random
import time

# Coordinates of the 22 cities including depot at index 0
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Number of robots
num_robots = 4

# Initial feasible solution
def initial_solution():
    cities = list(range(1, len(coordinates)))  # ignore depot at 0
    random.shuffle(cities)  # Random shuffle for initial distribution
    tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(cities):
        tours[i % num_robots].append(city)
    return tours

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = euclidean_distance(0, tour[0])  # from depot to first city
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], 0)  # from last city to depot
    return cost

# Shaking operation
def shake(tours, k):
    for _ in range(k):
        src_tour_id = random.randrange(num_robots)
        if len(tours[src_tour_id]) == 0:
            continue
        city = tours[src_tour_id].pop(random.randrange(len(tours[src_tour_id])))
        dest_tour_id = random.randrange(num_robots)
        tours[dest_tour_id].append(city)

# Local search by 2-opt
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(len(tour) - 1):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue
                if euclidean_distance(tour[i], tour[j]) + euclidean_distance(tour[(i+1) % len(tour)], tour[(j+1) % len(tour)]) < euclidean_distance(tour[i], tour[(i+1) % len(tour)]) + euclidean_distance(tour[j], tour[(j+1) % len(tour)]):
                    tour[i+1:j+1] = tour[i+1:j+1][::-1]
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

# Execute the algorithm and print results
tours = gvns()
max_cost = 0
for i, tour in enumerate(tours):
    tour_with_depot = [0] + tour + [0]
    cost = calculate_tour_cost(tour)
    max_cost = max(max_cost, cost)
    print(f"Robot {i} Tour: {tour_with_depot}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")