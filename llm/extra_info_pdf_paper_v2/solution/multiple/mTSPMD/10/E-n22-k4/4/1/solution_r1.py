import numpy as np
import math

# Compute Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Initialize city coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of depots and cities
num_depots = 4
num_cities = len(city_coordinates)

# Distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Number of robots
num_robots = 4
robot_depot_starts = [0, 1, 2, 3]

def ant_colony_optimization(num_ants=10, num_iterations=100, decay=0.95, alpha=1, beta=5):
    pheromone = np.ones(distance_matrix.shape) / len(city_coordinates)
    best_cost = float('inf')
    best_solution = []
    
    for iteration in range(num_iterations):
        all_tours = []
        for ant in range(num_ants):
            tours = []
            for robot in range(num_robots):
                tour = [robot_depot_starts[robot]]
                visited = set(tour)
                
                for _ in range((num_cities - num_depots) // num_robots):
                    current_city = tour[-1]
                    probabilities = []
                    for city in range(num_cities):
                        if city not in visited:
                            prob = pheromone[current_city][city] ** alpha * ((1.0 / (distance_matrix[current_city][city] + 1e-10)) ** beta)
                            probabilities.append((prob, city))
                    next_city = max(probabilities)[1] if probabilities else tour[0]
                    tour.append(next_city)
                    visited.add(next_city)
                tour.append(tour[0])  # conclude the tour
                tours.append(tour)
            all_tours.append(tours)
        
        # Evaluate and update pheromone
        for tours in all_tours:
            total_cost = 0
            for tour in tours:
                tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
                total_cost += tour_cost
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_solution = tours
            # Update pheromones
            for tour in tours:
                for i in range(len(tour) - 1):
                    pheromone[tour[i]][tour[i + 1]] *= (1 - decay)
                    pheromone[tour[i]][tour[i + 1]] += decay / tour_cost
    return best_solution, best_cost

# Run the optimization
best_tours, best_total_cost = ant_colony_optimization()

# Print outputs
for i, tour in enumerate(best_tours):
    tour_cost = sum(distance_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_total_cost}")