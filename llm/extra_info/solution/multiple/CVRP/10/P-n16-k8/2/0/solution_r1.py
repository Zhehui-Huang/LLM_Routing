import math
from itertools import permutations

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of Robots and their capacities
num_robots = 8
robot_capacity = 35

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate full distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Solution with simple heuristic
tours = [[] for _ in range(num_robots)]
tour_costs = [0] * num_robots
current_loads = [0] * num_robots
current_cities = [0] * num_robots  # All robots start at the depot

unserved_cities = set(range(1, len(demands)))  # Cities excluding the depot

# Assign cities to robots until all cities are served
while unserved_cities:
    for robot in range(num_robots):
        if not unserved_cities:
            break
        # Nearest neighbor heuristic: Choose the nearest city where demand <= remaining capacity
        nearest_city = None
        min_distance = float('inf')
        for city in unserved_cities:
            if demands[city] <= robot_capacity - current_loads[robot]:
                d = dist_matrix[current_cities[robot]][city]
                if d < min_distance:
                    min_distance = d
                    nearest_city = city
        if nearest_city is not None:
            # Update robot tour and costs
            tours[robot].append(nearest_robot)
            tour_costs[robot] += min_distance
            current_loads[robot] += demands[nearest_city]
            current_cities[robot] = nearest_city
            unserved_cities.remove(nearest_city)

# Close all tours returning to depot and update the cost
for robot in range(num_robots):
    if tours[robot]:
        tour_costs[robot] += dist_matrix[current_cities[robot]][0]
        tours[robot].append(0)  # return to depot
        tours[robot].insert(0, 0)  # start from depot
        
# Calculate and display total travel cost
total_travel_cost = sum(tour_costs)

# Display the output
for robot in range(num_robots):
    if tours[robot]:
        print(f"Robot {robot} Tour: {tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")
print(f"Overall Total Travel rentals