import math
import numpy as np

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Parameters
num_cities = len(coordinates)
num_robots = 4
depot = 0

# Calculate distances between all pairs of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Function to distribute cities to robots
def initial_solution():
    cities_per_robot = num_cities // num_robots
    tours = [[] for _ in range(num_robots)]
    assigned_cities = set()
    assigned_cities.add(depot)
    
    # Simple greedy distribution (sort cities by distance from depot and distribute sequentially)
    for r in range(num_robots):
        current_city = depot
        for _ in range(cities_per_robot if r < num_robots - 1 else num_cities - len(assigned_cities)):
            # Find nearest unassigned city
            nearest = None
            min_dist = float('inf')
            for city in range(num_cities):
                if city not in assigned_cities and distance_matrix[current_city][city] < min_dist:
                    nearest = city
                    min_dist = distance_matrix[current_city][city]
            assigned_cities.add(nearest)
            tours[r].append(nearest)
            currentSmarttask_city = nearest
    
    # Ensure each tour starts and ends at depot
    for tour in tours:
        tour.insert(0, depot)
        tour.append(depot)
    
    return tours

def compute_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Generate an initial solution
tours = initial_solution()

# Calculate and display the results
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = compute_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel IT cost: {total_cost}")