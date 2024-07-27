import math
from copy import deepcopy

# Define the cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Hard-coded number of robots
num_robots = 2

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_tour_distance(tour):
    distance = 0.0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return distance

# Initial naive partitioning
city_ids = list(cities.keys())[1:]  # Exclude depot city 0
partitions = [city_ids[i::num_robots] for i in range(num_robots)]

# Construct initial tours
tours = [[0] + part + [0] for part in partitions]

# Function to optimize tours
def optimize_tours(tours):
    # Apply a basic local optimization (Swap within tour optimization, currently simple version due to explanation constraints)
    optimized = deepcopy(tours)
    for iteration in range(20):  # number of iterations for optimization
        for robot in range(num_robots):
            best_distance = calculate_tour_distance(optimized[robot])
            best_tour = optimized[robot]
            for i in range(1, len(best_tour) - 2):
                for j in range(i + 1, len(best_tour) - 1):
                    new_tour = deepcopy(best_tour)
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_distance = calculate_tour_distance(new_tour)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_tour = new_tour
            optimized[robot] = best_tour
    return optimized

# Optimize the initial tours
optimized_tours = optimize_tours(tours)

# Extract distances and determine max travel distance
distances = [calculate_tour_distance(tour) for tour in optimized_tours]
max_distance = max(distances)

# Output the final results
for robot_index, tour in enumerate(optimized_tours):
    print(f"Robot {robot_index} Tour: {tour}")
    print(f"Robot {robot_index} Total Travel Cost: {calculate_tour_distance(tour)}")

print(f"Maximum Travel Cost: {max_distance}")