import math
import random

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialization of tours (greedy heuristic based on nearest cities)
def initialize_tours(cities, num_robots):
    sorted_cities = sorted(range(1, len(cities)), key=lambda x: euclidean_distance(cities[0], cities[x]))
    tours = {i: [0] for i in range(num_robots)}
    for index, city in enumerate(sorted_cities):
        min_tour = min(tours, key=lambda k: euclidean_distance(cities[tours[k][-1]], cities[city]))
        tours[min_tour].append(city)
    for t in tours:
        tours[t].append(0)
    return tours

# Calculate the cost of a tour
def calculate_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Shaking the solution by randomly swapping cities between tours
def shake(tours, k, cities):
    keys = list(tours.keys())
    while k > 0:
        r1, r2 = random.sample(keys, 2)
        if len(tours[r1]) > 2 and len(tours[r2]) > 2:
            i1, i2 = random.randint(1, len(tours[r1]) - 2), random.randint(1, len(tours[r2]) - 2)
            tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
            k -= 1
    return tours

# Variable Neighborhood Descent
def vnd(tours, l_max, cities):
    improved = True
    while improved:
        improved = False
        for l in range(1, l_max + 1):
            for t in tours:
                current_cost = calculate_tour_cost(tours[t], cities)
                best_local_solution = tours[t][:]
                for i in range(1, len(tours[t]) - 1):
                    for j in range(i + 1, len(tours[t]) - 1):
                        tours[t][i], tours[t][j] = tours[t][j], tours[t][i]
                        new_cost = calculate_tour_cost(tours[t], cities)
                        if new_cost < current_cost:
                            best_local_solution = tours[t][:]
                            current_cost = new_output
                            improved = True
                        else:
                            tours[t][i], tours[t][j] = tours[t][j], tours[t][i]  # revert
                tours[t] = best_local_solution
    return tours

# Implement the GVNS method
def gvns(cities, num_robots, k_max, l_max, t_max):
    random.seed(10)  # for reproducibility
    tours = initialize_tours(cities, num_robots)
    iteration = 0
    while iteration < t_max:
        k = 1
        while k < k_max:
            new_tours = shake(tours.copy(), k, cities)
            better_tours = vnd(new_tours, l_max, cities)
            if max(calculate_tour_cost(better_tours[t], cities) for t in better_tours) < max(calculate_tour_cost(tours[t], cities) for t in tours):
                tours = better_tours
                k = 1  # reset k
            else:
                k += 1
        iteration += 1
    return tours

# Define cities coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Constants for the GVNS
num_robots = 2
k_max = 5
l_max = 5
t_max = 100

# Execute the algorithm
solution_tours = gvns(cities, num_robots, k_max, l_max, t_max)

# Print results
max_cost = 0
for robot_id, tour in solution_tours.items():
    cost = calculate_tour_cost(tour, cities)
    max_cost = max(max_cost, cost)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")