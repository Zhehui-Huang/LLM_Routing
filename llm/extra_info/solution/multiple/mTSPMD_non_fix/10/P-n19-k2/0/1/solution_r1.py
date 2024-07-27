import numpy as np

# Cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and their starting depots
num_robots = 2
depot_indices = [0, 1]

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Function to find nearest neighbor tour
def nearest_neighbor_tour(start_city, cities_to_visit):
    unvisited = set(cities_to_visit)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    return tour

# Assign initial cities to each robot
def split_cities_among_robots():
    all_cities = set(range(len(coordinates)))
    robots_cities = {i: [depot_indices[i]] for i in range(num_robots)} # start with depots
    
    non_depot_cities = all_cities - set(depot_indices)
    available_cities = list(non_depot_cities)

    # Each robot starts doing tours from their respective depots
    for i in range(num_robots):
        current_city = depot_indices[i]
        while available_cities:
            next_city = min(available_cities, key=lambda x: euclidean_distance(current_city, x))
            if next_city in available_cities:
                robots_cities[i].append(next_city)
                available_cities.remove(next_city)
                current_city = next_city

    return robots_cities

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return cost

# Allocate cities to robots and create tours
robots_cities = split_cities_among_robots()
total_cost = 0

results = []
for robot_id, cities in robots_cities.items():
    tour = nearest_neighbor_tour(depot_indices[robot_id], cities[1:])  # cities[1:] to exclude the initial depot which is already considered
    tour_cost = calculate_tour_cost(tour)
    results.append((tour, tour_cost))
    total_cost += tour_cost

# Output the results
for robot_id, (tour, cost) in enumerate(results):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")