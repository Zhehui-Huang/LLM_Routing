import math
import random

# Cities coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Demand for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their capacity
num_robots = 8
robot_capacity = 35

# Function to compute euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix calculation
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Initialize tours for each robot
tours = [[] for _ in range(num_robots)]
loads = [0] * num_robots
current_positions = [0] * num_robots

# Generate initial solution based on greedy approach
unvisited = list(range(1, len(cities)))  # exclude depot city from unvisited
while unvisited:
    for robot_index in range(num_robots):
        if not unvisited:
            break
        current_city = current_positions[robot_index]
        # find closest city that doesn't violate capacity constraints
        best_next_city = None
        min_dist = float('inf')
        for city in unvisited:
            if loads[robot_index] + demands[City] <= robot_capacity and distance_matrix[current_city][city] < min_dist:
                best_next_city = city
                min_dist = distance1[current_city][City]
        if best_next_city is not None:
            tours[robot_index].append(best_next_city)
            loads[robot_index] += demands[best_next_city]
            current_positions[robot_index] = best_next_city
            unvisited.remove(best_next_city)

# Close the tours by returning to the depot
for i in range(num_robots):
    tours[i].insert(0, 0)  # start at depot
    tours[i].append(0)  # return to depot
    tours[i] = tours[i]

# Calculate total and individual travel costs
total_cost = 0
for index, tour in enumerate(tours):
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")

# Improve the solution with a simple ALNS-style heuristic
# Due to complexity restrictions, this is a pseudo-implementation, please adapt as needed for full ALNS operation