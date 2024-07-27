import numpy as np
from scipy.spatial.distance import cdist

# Coordinates of the cities including the depot
city_coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
])

# Number of robots
num_robots = 4

# Calculate the Euclidean distance matrix between each pair of cities
distance_matrix = cdist(city_coordinates, city_coordinates)

def greedy_round_robin_assignment():
    num_cities = len(city_coordinates) - 1  # ignore the depot city 0
    tours = {r: [0] for r in range(num_robots)}  # start at depot
    unvisited_cities = list(range(1, num_cities + 1))
    idx, steps = 0, 0
    while unvisited_cities:
        current_city = tours[idx % num_robots][-1]
        # Find the nearest neighbor
        next_city = min(unvisited_cities, key=lambda x: distance_matrix[current_city, x])
        tours[idx % num_robots].append(next_city)
        unvisited_cities.remove(next_city)
        idx += 1
    # Close the tours by returning to the depot
    for r in range(num_robots):
        tours[r].append(0)
    return tours

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def mTSP_solution():
    tours = greedy_round_robin_assignment()
    total_cost = 0
    for i in range(num_robots):
        tour = tours[i]
        tour_cost = calculate_tour_cost(tour)
        total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

mTSP_solution()