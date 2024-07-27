import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define coordinates for each city and depot
coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252],
    [163, 247], [146, 246], [161, 242], [142, 239], [163, 236],
    [148, 232], [128, 231], [156, 217], [129, 214], [146, 208],
    [164, 207], [141, 206], [147, 193], [164, 193], [129, 189],
    [155, 185], [139, 182]
])

def calculate_distance_matrix(coords):
    """Compute Euclidean distance matrix."""
    return np.array([[euclidean(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))])

def create_tours(robot_depots):
    robot_tours = {rd: [rd] for rd in robot_depots}
    visited = set(robot_depots)
    all_cities = set(range(len(coordinates)))

    unvisited = list(all_cities - visited)
    random.shuffle(unvisited)

    # Naive nearest-neighbour approach per robot
    for city in unvisited:
        nearest_robot = None
        min_distance = float('inf')

        # Find nearest robot depot for each city
        for rd in robot_depots:
            distance = distance_mtx[rd][city]
            if distance < min_distance:
                nearest_robot = rd
                min_distance = distance

        robot_tours[nearest(random_depots(city, distance_mtx))].append(city)

    # Ensure all tours are returned to their respective depots
    for rd in robot_depots:
        robot_tours[rd].append(rd)
    
    return robot_tours

def calculate_tour_cost(tour):
    return sum(distance_mtx[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Calculate distances between all pairs
distance_mtx = calculate_distance_matrix(coordinates)

# Define starting depots for each robot
depots = [0, 1, 2, 3]

# Generate initial tours for each robot
tours = create_tours(depots)

# Calculate and output tour and cost information
total_travel_cost = 0
for robot_id, tour in tours.items():
    tour_cost = calculate_tour_cost(tour)
    total_travel_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"\nOverall Total Travel Cost: {total_travel_ts_cost}")