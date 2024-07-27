import numpy as np
import random

# Define the cities and their coordinates
city_coords = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])

# Number of robots and their respective depot indices
num_robots = 8
depots = list(range(num_robots))

def calculate_distances():
    """Calculate Euclidean distances between each pair of cities."""
    num_cities = len(city_coords)
    distances = np.empty((num_cities, num_cities), dtype=np.float32)
    
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = np.sqrt(np.sum((city_coords[i] - city_coords[j]) ** 2))
    
    return distances

def initial_solution(num_robots, depots):
    """Generate a feasible initial solution based on nearest neighbor heuristic."""
    cities = list(range(len(city_coords)))
    tours = {depot: [depot] for depot in depots}

    available_cities = set(cities) - set(depots)
    for depot in depots:
        current_city = depot
        while available_cities:
            next_city = min(available_cities, key=lambda x: distances[current_city, x])
            tours[depot].append(next_city)
            available_cities.remove(next_city)
            current_city = next_city
        
        # Return to depot
        tours[depot].append(depot)
        
        # Assign each robot roughly an equal number of non-depot cities
        if len(available_cities) == 0:
            break

    return tours

def calculate_tour_cost(tour, distances):
    """Calculate the total cost of a tour."""
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Calculate distances between all cities
distances = calculate_distances()

# Create an initial solution
initial_tours = initial_solution(num_robots, depots)

# Display initial tours and calculate costs
total_cost = 0
for robot_id, tour in initial_tours.items():
    cost = calculate_tour_cost(tour, distances)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_size} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")