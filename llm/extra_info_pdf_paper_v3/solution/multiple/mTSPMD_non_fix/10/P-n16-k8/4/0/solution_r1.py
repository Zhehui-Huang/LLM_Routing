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

# Simulated Annealing function
def simulated_annealing(initial_tour):
    def total_distance(tour):
        return sum(distance_matrix[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour)))
    
    current_tour = initial_tour[:]
    current_cost = total_distance(current_tour)
    T = 1.0
    T_min = 0.00001
    cooling_rate = 0.99
    
    while T > T_min:
        i = random.randint(0, len(current_tour) - 1)
        j = random.randint(0, len(current_tour) - 1)

        # Swap two cities in the tour
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        # Calculate new tour cost
        new_cost = total_distance(new_tour)

        # Decide if we should accept the new tour
        if new_cost < current_cost or math.exp((current_cost - new_cost) / T) > random.random():
            current_tour = new_tour
            current_cost = new_cost

        T *= cooling_rate

    return current_tour, current_cost

# Prepare the city indices excluding the depot
city_indices = list(range(1, n_cities))

# Randomly assign cities to robots, only start indexed '0' is fixed
random.shuffle(city_indices)
segment_size = len(city_indices) // num_robots

robot_tours = []
overall_total_cost = 0

# Creating tours for each robot
for i in range(num_robots):
    start_index = i * segment_size
    end_index = start_index + segment_size if i != num_robots - 1 else len(city_indices)
    
    # Include the starting depot and prepare tour segment
    tour_segment = [0] + city_indices[start_index:end_index]
    tour, cost = simulated_annealing(tour_segment)
    
    robot_tours.append(tour)
    overall_total_cost += cost
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")