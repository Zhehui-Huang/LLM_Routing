import numpy as np
import math

# Environment setup
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate distances matrix
num_cities = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# ACO Parameters
antnum = 10
cyclenum = 100
inittrail = 0.1
alpha = 1.0
beta = 2.0
rho = 0.5

# Initialize pheromones
pheromones = [[inittrail for _ in range(num_cities)] for _ in range(num_cities)]

def feasible_next_cities(current_city, visited):
    return [c for c in range(num_cities) if c not in visited]

def aco_tsp(robot_start):
    best_tour = None
    best_cost = float('inf')
    
    for cycle in range(cyclenum):
        all_tours = []
        
        for ant in range(antnum):
            tour = [robot_start]
            unvisited = set(range(num_cities)) - {robot_start}
            
            while unvisited:
                current_city = tour[-1]
                feasible_cities = feasible_next_cities(current_city, tour)
                
                if not feasible_cities:
                    break
                
                probabilities = []
                for city in feasible_cities:
                    phero = pheromones[current_city][city] ** alpha
                    heuristic = (1 / distances[current_city][city]) ** beta if distances[current_city][city] != 0 else 0
                    probabilities.append(phero * heuristic)
                
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(feasible_cities, p=probabilities)
                tour.append(next_city)
                unvisited.remove(next_city)
            
            tour.append(robot_start)
            all_tours.append(tour)
        
        # Update pheromones
        pheromones = [[(1 - rho) * pheromones[i][j] for j in range(num_cities)] for i in range(num_cities)]
        
        # Add new pheromone
        for tour in all_tours:
            tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i + 1]] += 1 / tour_cost
            
            if tour_cost < best_cost:
                best_tour = tour
                best_cost = tour_cost

    return best_tour, best_cost

# Find routes for each robot
tour0, cost0 = aco_tsp(0)
tour1, cost1 = aco_tsp(1)

# Print results
print("Robot 0 Tour:", tour0)
print("Robot 0 Total Travel Cost:", cost0)
print("Robot 1 Tour:", tour1)
print("Robot 1 Total Travel Cost:", cost1)
print("Overall Total Travel Cost:", cost0 + cost1)