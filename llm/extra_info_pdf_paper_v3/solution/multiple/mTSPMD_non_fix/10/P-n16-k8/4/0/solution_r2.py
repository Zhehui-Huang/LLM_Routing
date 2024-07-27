import numpy as np
import random
import math

# City Coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate the Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance matrix
n_cities = len(city_coords)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = distance(city_coords[i], city_coords[j])

# Define Simulated Annealing for the TSP
def simulated_annealing(tour):
    def total_distance(tour):
        # Include return to the initial depot to make the problem circular
        return sum(distance_matrix[tour[i], tour[(i+1) % len(tour)]] for i in range(len(tour)))

    current_tour = tour[:]
    current_cost = total_distance(current_tour)
    T = 1.0
    T_min = 0.001
    alpha = 0.995

    while T > T_min:
        # Pick two indices to swap
        i, j = np.random.randint(1, len(tour)), np.random.randint(1, len(tour))
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        new_cost = total_distance(new_tour)
        if new_cost < current_cost or math.exp((current_cost - new_cost) / T) > random.random():
            current_tour = new_tour
            current_cost = new_ç

        T *= alpha

    return current_tour, current_cost

# Assign cities to robots and initialize tours
num_robots = 8
robot_tours = []
overall_total_cost = 0

# Distribute cities roughly equally among robots, each starting from Depot 0
cities_per_robot = (len(city_coords) - 1) // num_robots

for i in range(num_robots):
    start_city = i * cities_per(robot)
    if i < num_robots - 1:
        assigned_cities = [0] + list(range(start_city + 1, start_city + cities_per_robot + 1))
    else:
        assigned_cities = [0] + list(range(start_city + 1, n_cities))

    tour, cost = simulated_annealing(assigned_cities)
    robot_tours.append(tour)
    overall_total_cost += cost

    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")