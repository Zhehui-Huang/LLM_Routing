import numpy as np

# City coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Define robots' depot assignments
depots = {i: i for i in range(8)}

# Compute the Euclidean distance between cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        
# Greedy approach to assign cities to nearest robot's route
tours = {robot: [robot] for robot in depots.keys()}
remaining_cities = set(range(num_cities)) - set(depots.keys())

for robot in depots:
    current_city = robot
    while remaining_cities:
        nearest_city = min(remaining_cices, key=lambda city: distance_matrix[current_city][city])
        if nearest_city not in depots.values():  # avoid selecting another depot as part of the tour
            tours[robot].append(nearest_city)
            remaining_cities.remove(nearest_city)
            current_city = nearest_city

    # Finally, return to the robot's starting depot
    tours[robot].append(robot)

# Compute the travel costs for each tour and the overall cost
overall_total_cost = 0
for robot, tour in tours.items():
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")