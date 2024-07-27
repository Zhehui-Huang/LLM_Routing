import numpy as np
import random
import math

# City Coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance matrix
n_cities = len(city_coords)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = distance(city_coords[i], city_coords[j])

# Simulated Annealing to find the optimal tour
def simulated_annealing(cities):
    def total_distance(tour):
        return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    current_tour = cities[:]
    random.shuffle(current_tour)
    current_cost = total_distance(current_tour)
    T = 1.0
    T_min = 0.00001
    cooling_rate = 0.9
    
    while T > T_min:
        i = random.randint(1, len(current_tour) - 2)
        j = random.randint(1, len(current_tour) - 2)
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = total_distance(new_tour)

        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / T):
            current_tour = new_tour
            current_cost = new_cost

        T *= cooling_rate

    return current_tour, current_cost

# Assign cities to robots, we have 8 robots starting from Depot 0
num_robots = 8
cities_per_robot = len(city_coords) // num_robots

tours = []
total_cost = 0

# Create and optimize tours
for i in range(num_robots):
    start = (i * cities_per_robot) if i < num_robots - 1 else cities_per_robot * (num_robots - 1)
    end = start + cities_per_robot if i < num_robots - 1 else len(city_coords)
    
    assigned_cities = [0] + list(range(start + 1, end + 1))
    tour, cost = simulated_annealing(assigned_cities + [0])  # starts and ends at depot 0
    tours.append(tour)
    total_cost += cost

    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")