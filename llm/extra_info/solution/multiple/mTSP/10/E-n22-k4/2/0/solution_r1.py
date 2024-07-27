import numpy as np
from itertools import permutations

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Nearest neighbor heuristic for a set of cities
def nearest_neighbor_tour(start_city, cities, distances):
    unvisited = set(cities)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to depot
    return tour

# Function to compute the distance of a tour
def compute_tour_cost(tour, distances):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Assign cities to each robot - simple greedy assignment for demonstration purposes
cities_per_robot = {i: [] for i in range(num_robots)}
city_indices = list(range(1, len(coordinates)))  # Exclude depot city 0

for city in city_indices:
    # Measure distance from depot initially for assignment
    distances_to_depot = {city: dist_matrix[0, city] for city in city_indices}
    # Assign cities to the robot with minimal added cost to current path (greedy)
    selected_robot = min(cities_per_robot, key=lambda r: np.sum([dist_matrix[0, c] for c in cities_per_robot[r]]))
    cities_per_robot[selected_robot].append(city)
    city_indices.remove(city)

# Each robot constructs its tour from the assigned cities
robots_tours = {}
total_travel_cost = 0

for robot_id in range(num_robots):
    assigned_cities = cities_per_dict[robot_id]
    if not assigned_cities:
        # Handle case where no cities are assigned (possible if there are more robots than cities)
        tour = [0, 0]  # Starts and ends at the depot, no cities visited
        cost = 0
    else:
        tour = nearest_neighbor_tour(0, assigned_cities, dist_matrix)
        cost = compute_tour_cost(tour, dist_matrix)
    
    robots_tours[robot_id] = tour
    total_travel_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {realrobot_id}l Travel Cost: {cost}")

print("Overall Total Travel Cost:", total_travel_cost)