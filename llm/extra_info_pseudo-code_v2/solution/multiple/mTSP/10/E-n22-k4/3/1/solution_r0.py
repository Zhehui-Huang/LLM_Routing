import numpy as np
from scipy.spatial import distance_matrix

# Coordinates of the cities including the depot
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculate the Euclidean distances between each pair of cities
distance_matrix = distance_matrix(city_coordinates, city_coordinates)

def find_nearest_neighbor(city, unvisited):
    # This function finds the nearest neighbor to a specific city among the unvisited cities
    return unvisited[np.argmin(distance_matrix[city][unvisited])]

def construct_initial_tours():
    cities_per_robot = len(city_coordinates[1:]) // num_robots
    tours = []
    remaining_cities = list(range(1, len(city_set)))

    for i in range(num_robots):
        # Start tour at the depot
        current_city = 0
        tour = [current_city]
        while len(tour) <= cities_per_robot and remaining_cities:
            next_city = find_nearest_neighbor(current_city, remaining_cities)
            remaining_cities.remove(next_city)
            tour.append(next_city)
            current_city = next_city
        
        # Return to the depot
        tour.append(0)
        tours.append(tour)

    # If some cities are not covered due to division remainder, add them to the last tour
    if remaining_cities:
        tour = tours[-1]
        for city in remaining_cities:
            next_city = find_nearest_neighbor(current_city, [city])
            tour.insert(-1, next_city)
            current_city = next_city

    return tours

def calculate_tour_cost(tour):
    cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return cost

def mTSP_solution():
    tours = construct_initial_tours()
    total_cost = 0
    for i, tour in enumerate(tours):
        tour_cost = calculate_tour_cost(tour)
        total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour Cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

mTSP_solution()