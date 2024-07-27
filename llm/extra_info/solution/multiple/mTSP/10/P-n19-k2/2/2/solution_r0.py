import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Define the cities coordinates with indices corresponding to city numbers
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Convert dictionary to array for processing
city_array = np.array(list(cities.values()))

# Calculate the Euclidean distances between each pair of cities
dist_matrix = cdist(city_array, city_array)

def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i-1], tour[i]] for i in range(1, len(tour)))

def nearest_insertion(depot, cities, dist_matrix):
    tour = [depot, 0]
    unvisited = set(cities)
    unvisited.remove(depot)
    
    while unvisited:
        # Finds the nearest unvisited city to the current tour
        insertion = min((dist_matrix[tour[i], city], i + 1, city) for i in tour[:-1] for city in unvisited)
        _, position, city = insertion
        tour.insert(position, city)
        unvisited.remove(city)
    return tour

# Assigning cities to robots using K-Means clustering based on their locations
kmeans = KMeans(n_clusters=2, random_state=0).fit(city_array[1:])  # Exclude the depot city for clustering
labels = kmeans.labels_

# Organize cities by assigned robot
robot_1_cities = [0]  # Include the depot
robot_2_cities = [0]  # Include the depot
for i, label in enumerate(labels, 1):
    if label == 0:
        robot_1_cities.append(i)
    else:
        robot_2_cities.append(i)

# Find optimised TSP tour for each robot
robot_1_tour = nearest_insertion(0, robot_1_cities, dist_matrix)
robot_2_tour = nearest_insertion(0, robot_2_cities, dist_matrix)

# Calculate individual and total travel costs
robot_1_cost = calculate_tour_cost(robot_1_tour)
robot_2_cost = calculate_tour_cost(robot_2_tour)
total_cost = robot_1_cost + robot_2_cost

# Print the outputs
print(f"Robot 0 Tour: {robot_1_tour}")
print(f"Robot 0 Total Travel Cost: {robot_1_cost:.2f}")
print(f"Robot 1 Tour: {robot_2_tour}")
print(f"Robot 1 Total Travel Cost: {robot_2_cost:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")