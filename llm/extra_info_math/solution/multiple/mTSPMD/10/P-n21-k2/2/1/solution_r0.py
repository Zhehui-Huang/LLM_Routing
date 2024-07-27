from scipy.spatial import distance_matrix
import numpy as np

# Define the city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Compute the distance matrix
locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(locations, locations)

# Function to calculate total travel cost for a route
def calculate_cost(route, dist_matrix):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

# Heuristic: Assign cities to closest depot
tours = {0:[0], 1:[1]}  # Both robots start at their depots

for city in range(2, len(cities)):
    # Assign city to the closest depot
    if dist_matrix[0][city] < dist_matrix[1][city]:
        tours[0].append(city)
    else:
        tours[1].append(city)

# Close the tours at their respective depots
tours[0].append(0)
tours[1].append(1)

# Calculate the cost of each tour
robot_0_cost = calculate_cost(tours[0], dist_matrix)
robot_1_cost = calculate_cost(tours[1], dist_matrix)

# Calculate the total cost
total_cost = robot_0_cost + robot_1_cost

# Print the outputs
print("Robot 0 Tour:", tours[0])
print("Robot 0 Total Travel Cost:", round(robot_0_cost, 2))
print("Robot 1 Tour:", tours[1])
print("Robot 1 Total Travel Cost:", round(robot_1_cost, 2))
print("Overall Total Travel Cost:", round(total_cost, 2))