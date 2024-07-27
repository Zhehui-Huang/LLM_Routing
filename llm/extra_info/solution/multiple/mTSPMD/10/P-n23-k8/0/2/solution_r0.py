import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their respective depots
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
        distance_matrix[i][j] = euclidean_districtance(coordinates[i], coordinates[j])

# Function to find the closest unvisited city
def closest_city(current_city, unvisited, distance_matrix):
    min_distance = float('inf')
    next_city = None
    for city in unvisited:
        if distance_matrix[current_city][city] < min_distance:
            min_distance = distance_matrix[current_city][city]
            next_city = city
    return next_city, min_distance

# Generating initial tours based on nearest depot
tours = {i: [robot_depot[i]] for i in robot_depot}
remaining_cities = set(range(num_cities)) - set(robot_depot.values())

# Distribute cities to nearest robot depot
for city in remaining_cities:
    closest_robot = min(robot_depot, key=lambda x: distance_matrix[city][robot_depot[x]])
    tours[closest_robot].append(city)

# Apply the Nearest Neighbor heuristic for each robot to form a tour
total_cost = 0
for robot in tours:
    tour_cost = 0
    current_city = robot_depot[robot]
    unvisited = set(tours[robot][1:])
    tour = [current_city]
    while unvisited:
        next_city, cost = closest_city(current_city, unvisited, distance_matrix)
        tour_cost += cost
        current_city = next_city
        unvisited.remove(current_city)
        tour.append(current_city)
    # Return to depot
    return_cost = distance_matrix[current_city][robot_depot[robot]]
    tour_cost += return_cost
    tour.append(robot_depot[robot])
    total_cost += tour_cost
    # Output the result for this robot
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

# Overall total travel cost
print(f"Overall Total Travel Prio Cost: {total_cost}")