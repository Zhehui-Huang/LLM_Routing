import math
import random

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of Robots and their start/end locations
num_robots = 8
depots = list(range(num_robots))

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
num_cities = len(city_coordinates)
distances = [
    [euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# ACO parameters
antnum = 20
alpha = 1.0
beta = 5.0
rho = 0.1
inittrail = 1.0 / num_cities
cyclenum = 100

# Initialize pheromones
pheromones = [[inittrail]*num_cities for _ in range(num_cities)]

def calculate_transition_probabilities(current, allowed, pheromones, distances):
    pheros = [pheromones[current][j]**alpha * (1 / distances[current][j])**beta for j in allowed]
    total = sum(pheros)
    return [phero / total for phero in pheros]

def aco_tsp_for_single_robot(depot):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(cyclenum):
        all_ants_tours = []
        
        for _ in range(antnum):
            tour = [depot]
            unvisited = set(range(num_cities)) - {depot}
            
            current_city = depot
            
            while unvisited:
                allowed = list(unvisited)
                probs = calculate_transition_probabilities(current_city, allowed, pheromones, distances)
                next_city = random.choices(allowed, weights=probs)[0]
                
                tour.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city
            
            tour.append(depot)  # Return to depot
            all_ants_tours.append(tour)
        
        # Update pheromone
        for i in range(num_cities):
            for j in range(num_cities):
                pheromones[i][j] *= (1 - rho)
        
        for tour in all_ants_tours:
            tour_cost = sum(distances[tour[k]][tour[k+1]] for k in range(len(tour)-1))
            if tour_cost < best_cost:
                best_tour = tour
                best_cost = tour_cost
            
            for k in range(len(tour)-1):
                pheromones[tour[k]][tour[k+1]] += 1 / tour_cost
    
    return best_tour, best_cost

overall_total_cost = 0
for robot_id in depots:
    tour, cost = aco_tsp_for_single_robot(robot_id)
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")