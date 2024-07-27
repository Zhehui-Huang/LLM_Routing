import math
import itertools

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11,
    12, 26, 17, 6, 15, 5, 10
]

# Constants
num_robots = 8
robot_capacity = 40

def euclidean_distance(from_city, to_city):
    return math.sqrt((coordinates[to_city][0] - coordinates[from_city][0]) ** 2 + 
                     (coordinates[to_city][1] - coordinates[from_city][1]) ** 2)

# Initialize tours and track demands
tours = [[] for _ in range(num_robots)]
current_capacities = [0] * num_robots

def find_next_city(current_city, remaining_cities, robot_capacity, current_load):
    best_city = None
    min_distance = float('inf')
    for city in remaining_cities:
        if current_load + demands[city] <= robot_capacity:
            distance = euclidean_distance(current_city, city)
            if distance < min_distance:
                min_distance = distance
                best_city = city
    return best_city

# Assign cities to robots
remaining_cities = set(range(1, len(coordinates)))  # Exclude depot
current_city = [0] * num_robots  # Start at depot

while remaining_cities:
    for i in range(num_robots):
        if remaining_cities:
            next_city = find_next_city(current_city[i], remaining_cities, robot_capacity, current_capacities[i])
            if next_city is not None:
                tours[i].append(next_city)
                remaining_cities.remove(next_city)
                current_capacities[i] += demands[next_city]
                current_city[i] = next_city

# Close the tours returning to the depot
for i in range(num_robots):
    if tours[i]:
        tours[i] = [0] + tours[i] + [0]

# Calculate and print the tour details
total_cost = 0
for i in range(num_robots):
    tour_cost = sum(euclidean_distance(tours[i][j], tours[i][j + 1]) for j in range(len(tours[i]) - 1))
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}\n")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")