import numpy as np
import math

# Data: cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Parameters
num_robots = 8
depot = 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Build the distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Assign cities to robots
city_indices = list(range(1, len(cities)))  # excluding the depot
np.random.shuffle(city_indices)  # Random shuffle for initial assignment
chunks = np.array_split(city_indices, num_robots)  # Split cities into chunks

def nearest_neighbor_tour(start, cities):
    tour = [start]
    unvisited = cities[:]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # return to depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Initial tours using nearest neighbor heuristic
tours = [nearest_neighbor_tour(depot, list(chunk)) for chunk in chunks]

# Function for applying 2-opt optimization
def apply_2opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tournament) - 2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue  # adjacent edges are not considered
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Improve tours with 2-opt
optimized_tours = [apply_2opt(tour) for tour in tours]

# Calculate costs
tour_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
overall_cost = sum(tour_costs)

# Return the result
for i, tour in enumerate(optimized_tours):
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {tour_costs[i]:.2f}')

print(f'Overall Total Travel with Depots Travel Cost: {overall_cost:.2f}')