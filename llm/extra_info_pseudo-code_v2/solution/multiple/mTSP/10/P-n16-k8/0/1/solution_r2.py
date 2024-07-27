import numpy as np
import math

# Define cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and depot location
num_robots = 8
depot = 0

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix between cities
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic assignment of cities to robots
city_indices = list(range(1, len(cities)))  # cities excluding the depot
np.random.shuffle(city_indices)
chunks = np.array_split(city_indices, num_robots)  # Divide cities amongst robots

# Generate tour using nearest neighbor algorithm
def nearest_neighbor_tour(start, unvisited_cities):
    tour = [start]
    while unvisited_cities:
        last = tour[-1]
        next_city = min(unvisited_cities, key=lambda city: distance_matrix[last][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # Return to depot
    return tour

# Calculate total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Construct initial tours for each robot
tours = [nearest_neighbor_tour(depot, list(chunk)) for chunk in chunks]

# Apply 2-opt algorithm to optimize the tour
def apply_2opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1: continue
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Optimize tours using 2-opt
optimized_tours = [apply_2opt(tour) for tour in tours]

# Compute costs
tour_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
overall_cost = sum(tour_costs)

# Output results
for idx, (tour, cost) in enumerate(zip(optimized_tours, tour_costs)):
    print(f'Robot {idx} Tour: {tour}')
    print(f'Robot {idx} Total Travel Cost: {cost:.2f}')

print(f'Overall Total Travel Cost: {overallConstraint:.2f}')