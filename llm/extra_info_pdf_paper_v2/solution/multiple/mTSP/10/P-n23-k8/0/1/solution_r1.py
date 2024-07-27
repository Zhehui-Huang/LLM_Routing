import numpy as np
import random

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), 
    (37, 52), 
    (49, 49), 
    (52, 64), 
    (31, 62), 
    (52, 33), 
    (42, 41), 
    (52, 41), 
    (57, 58), 
    (62, 42), 
    (42, 57), 
    (27, 68), 
    (43, 67), 
    (58, 48), 
    (58, 27), 
    (37, 69), 
    (38, 46), 
    (61, 33), 
    (62, 63), 
    (63, 69), 
    (45, 35), 
    (32, 39), 
    (56, 37)
]

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the matrix of distances between each pair of cities
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

num_robots = 8

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    cost = distance_matrix[0, tour[0]]  # from depot to first city
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1], tour[i]]
    cost += distance_matrix[tour[-1], 0]  # from last city back to depot
    return cost

# Splitting the list of cities into almost equal parts for each robot
def split_cities(cities, num_robots):
    split_size = len(cities) // num_robots
    return [cities[i*split_size:(i+1)*split_size] for i in range(num_robots - 1)] + [cities[(num_robots-1)*split_size:]]

# Generating initial routes randomly
cities_to_visit = list(range(1, n_cities))  # city indices excluding the depot
random.shuffle(cities_to_visit)
robot_tours = split_cities(cities_to_visit, num_robots)

# Calculate and print out the results
overall_total_cost = 0
print(f"Generated tours and costs for each of the {num_robots} robots:")
for idx, tour in enumerate(robot_tours):
    tour_with_depot = [0] + tour + [0]
    tour_cost = calculate_tour_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour_with_depot}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")