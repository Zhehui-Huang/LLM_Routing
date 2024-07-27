import math
import random
from scipy.spatial import distance_matrix

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance
def euclidean_dist(i, j):
    xi, yi = cities[i]
    xj, yj = cities[j]
    return math.sqrt((xi - xj)**2 + (yi - yj)**2)

# Simulated annealing algorithm to optimize tour
def simulated_annealing(tour):
    def calculate_total_cost(tour):
        return sum(euclidean_dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    current_tour = tour[:]
    current_cost = calculate_total_cost(current_tour)
    T = 10000
    alpha = 0.99
    min_temp = 1

    while T > min_temp:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = calculate_total_cost(new_tour)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_tour, current_cost = new_tour, new_cost
        T *= alpha

    return current_tour, current_cost

# Distribute cities to 8 robots starting from the depot city
num_robots = 8
cities_per_robot = (len(cities) - 1) // num_robots
robot_tours = []

# Create a tour for each robot
all_cities = list(cities.keys())[1:]  # avoiding the depot in initial assignment
random.shuffle(all_cities)  # to randomize the city distribution

for i in range(num_robots):
    start_index = i * cities_per_robot
    if i < num_robots - 1:
        part = all_cities[start_index:start_index + cities_per_robot]
    else:
        part = all_cities[start_index:]  # Include any remaining cities in the last robot's tour
    tour = [0] + part + [0]  # start and end at the depot
    robot_tours.append(tour)

# Optimize each robot's tour using simulated annealing and calculate costs
results = []
total_cost = 0

for tour in robot_tours:
    opt_tour, opt_cost = simulated_annealing(tour)
    results.append((opt_tour, opt_cost))
    total_cost += opt_cost

for idx, (tour, cost) in enumerate(results):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")