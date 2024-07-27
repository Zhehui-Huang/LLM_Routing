import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Cities: ID and Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Converting city coordinates to a usable format
city_coords = np.array([coord for coord in cities.values()])

# Applying KMeans for initial clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords)

# Assigning cities to clusters
clusters = kmeans.labels_

# Function for calculating Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Building initial tours for each robot
tours = {i: [0] for i in range(num_robots)}  # initialize each tour with the depot
for city_index, cluster_index in enumerate(clusters):
    if city_index != 0:  # excluding depot city from tour destinations
        tours[cluster_index].append(city_index + 1)  # city indices are 1-based except the depot

# Closing the tours back at the depot
for tour in tours.values():
    tour.append(0)

# Function to calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(city_coords[tour[i]-1], city_coords[tour[i+1]-1])
    return cost

# Calculate and print each tour and cost
max_travel_cost = 0
for robot_id, tour in tours.items():
    cost = calculate_tour_cost(tour)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")
    if cost > max_travel_cost:
        max_travel_token = robot_id
        max_travel_cost = cost

# Print maximum travel cost
print(f"Maximum Travel Cost: {max_travel_cost:.2f}")