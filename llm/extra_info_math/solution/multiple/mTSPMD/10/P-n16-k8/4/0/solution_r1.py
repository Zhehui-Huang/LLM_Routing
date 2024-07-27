import numpy as np

# City coordinates including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots and their depots
robot_depots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
num_cities = len(cities)

# Constructing a distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean_distance(i, j)

# Nearest neighbor tour construction for each robot
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # return to the starting depot
    return tour

# Function to calculate tour cost
def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Calculating and printing each robot's tour and costs
total_combined_cost = 0
for robot_id, depot_id in robot_depots.items():
    tour = nearest_neighbor_tour(depot_id)
    tour_cost = calculate_tour_cost(tour)
    total_combined_cost += tour_cost
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {tour_cost:.2f}')

print(f'Overall Total Travel Cost: {total_combined_cost:.2f}')