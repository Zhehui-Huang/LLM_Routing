import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Prepare the robot depot assignments
robot_depot = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Euclidean distance calculator
def euclidean_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Distance matrix calculation
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighbor algorithm implementation for TSP solving
def nearest_neighbor_tour(start, distance_matrix):
    tour = [start]
    unvisited = set(range(num_cities)) - {start}
    current_city = start
    tour_length = 0
    
    while unvisited:
        nearest_city, min_dist = min(((city, distance_matrix[current_city][city]) for city in unvisited), key=lambda x: x[1])
        tour.append(nearest_city)
        tour_length += min_dist
        current_city = nearest_city
        unvisited.remove(nearest_city)
    
    # Closing the tour by returning to the depot
    tour_length += distance_matrix[current_city][start]
    tour.append(start)
    
    return tour, tour_length

# Solving TSP for each robot based on its depot starting point
total_travel_cost = 0
tours = []

for robot_id, start in robot_deport.items():
    robot_tour, tour_cost = nearest_neighbor_tour(start, distance_matrix)
    total_travel_cost += tour_cost
    tours.append((robot_id, robot_tour, tour_cost))
    
    # Output the output format results
    print(f"Robot {robot_id} Tour: {robot_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")