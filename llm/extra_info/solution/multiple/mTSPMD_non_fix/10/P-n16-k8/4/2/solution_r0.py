import numpy as np
from scipy.spatial import distance_matrix

# City coordinates with (index, (x, y)) mapping
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8
# Initial starting city for all robots
start_city = 0

# Compute matrix of distances between each pair of cities
cities = list(city_ordinates.values())
distance_matrix = distance.cdist(cities, cities, metric='euclidean')

def nearest_neighbor_tours(start_city, num_robots, distance_matrix):
    num_cities = len(distance_matrix)
    visited = np.zeros(num_cities, dtype=bool)
    visited[start_city] = True
    tours = [[] for _ in range(num_robots)]
    robot_positions = [start_city for _ in range(num_robots)]
    remaining_cities = list(range(num_cities))
    remaining_cities.remove(start_city)

    # Distribute initial cities to each robot
    for i in range(num_robots):
        nearest_city = min(remaining_cities, key=lambda c: distance_matrix[robot_positions[i], c])
        tours[i].append(nearest_city)
        robot_positions[i] = nearest_city
        visited[nearest_city] = True
        remaining_cities.remove(nearest_city)

    # Assign remaining cities to the nearest robot tour
    while remaining_cities:
        nearest_city, chosen_robot = min(
            ((city, robot_id) for city in remaining_cities for robot_id in range(num_robots)),
            key=lambda x: distance_matrix[robot_positions[x[1]], x[0]]
        )
        tours[chosen_robot].append(nearest_city)
        robot_positions[chosen_robot] = nearest_city
        visited[nearest_city] = True
        remaining_cities.remove(nearest_city)
        
    return tours

tours = nearest_neighbor_tours(start_city, num_robots, distance_matrix)

def calculate_cost(tours, distance_matrix):
    total_travel_cost = 0
    costs = []
    
    for tour in tours:
        cost = 0
        for i in range(1, len(tour)):
            cost += distance_matrix[tour[i - 1], tour[i]]
        costs.append(cost)
        total_travel_cost += cost
    
    return costs, total_travel_cost

costs, total_travel_cost = calculate_cost(tours, distance_matrix)

# Print the solution
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: [{start_city} -> {' -> '.join(map(str, tour))}]")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {total_travel_cost}")