import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of Robots and their capacities
num_robots = 8
robot_capacity = 35

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate full distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initialize tours and costs
tours = [[0] for _ in range(num_robots)]
tour_costs = [0.0 for _ in range(num_robots)]
current_loads = [0 for _ in range(num_robots)]

# Assign cities to robots 
remaining_cities = set(range(1, len(demands)))  # Exclude depot

# Function to find next city
def find_next_city(current_city, load):
    next_city = None
    min_dist = float('inf')

    for city in remaining_cities:
        if demands[city] + load <= robot_capacity:
            d = dist_matrix[current_city][city]
            if d < min_dist:
                min_dist = d
                next_city = city
    return next_city, min_dist

while remaining_cities:
    for i in range(num_robots):
        while True:
            next_city, dist = find_next_city(tours[i][-1], current_loads[i])
            if next_city is None:
                break  # No valid next city or capacity exceeded
            tours[i].append(next_city)
            tour_costs[i] += dist
            current_loads[i] += demands[next_city]
            remaining_cities.remove(next_city)

        # Return to depot
        return_dist = dist_matrix[tours[i][-1]][0]
        tour_costs[i] += return_dist
        tours[i].append(0)  # Complete the loop returning to the depot

# Calculate the output details
total_cost = sum(tour_costs)

# Display the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")