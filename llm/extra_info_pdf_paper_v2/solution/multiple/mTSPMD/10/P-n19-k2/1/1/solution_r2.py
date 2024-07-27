import math
import random

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def initialize_pheromone_matrix(num_cities, initial_pheromone):
    return [[initial_pheromone for _ in range(num_cities)] for _ in range(num_cities)]

def calculate_total_cost(tours, coordinates):
    total_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def update_pheromones(pheromones, tours, cost, evaporation_rate):
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= (1 - evaporation_rate)
    
    for tour in tours:
        tour_contribution = 1 / cost
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i+1]] += tour_contribution
            pheromones[tour[i+1]][tour[i]] += tour_contribution  # symmetric

def choose_next_city(current_city, coordinates, pheromones, visited, alpha, beta):
    choices = []
    for city in range(len(coordinates)):
        if city not in visited:
            prob = (pheromones[current_city][city] ** alpha) * ((1 / euclidean_distance(coordinates[current_city], coordinates[city])) ** beta)
            choices.append((prob, city))
    if not choices:
        return None
    total = sum(prob for prob, city in choices)
    if total == 0:
        return random.choice([city for prob, city in choices])
    r = random.uniform(0, total)
    sum_prob = 0
    for prob, city in choices:
        sum_prob += prob
        if sum_prob > r:
            return city

def aco_mTSP(coordinates, num_robots, num_iterations, num_ants, alpha, beta, evaporation_rate, initial_pheromone):
    num_cities = len(coordinates)
    pheromones = initialize_pheromone_matrix(num_cities, initial_pheromone)
    best_tours = None
    best_cost = float('inf')
    
    for _ in range(num_iterations):
        for _ in range(num_ants):
            tours = [[] for _ in range(num_robots)]
            visited = set()
            current_cities = [i for i in range(num_robots)]
            
            for i in range(num_robots):
                tours[i].append(current_cities[i])
                visited.add(current_cities[i])
            
            while len(visited) < num_cities:
                for robot_id in range(num_robots):
                    current_city = tours[robot_id][-1]
                    next_city = choose_next_city(current_city, coordinates, pheromones, visited, alpha, beta)
                    if next_city is not None:
                        tours[robot_id].append(next_city)
                        visited.add(next_city)

            for robot_id in range(num_robots):
                tours[robot_id].append(tours[robot_id][0])  # complete the cycle
            
            cost = calculate_total_cost(tours, coordinates)
            if cost < best_cost:
                best_cost = cost
                best_tours = tours
            
            update_pheromones(pheromones, tours, cost, evaporation_rate)
    
    return best_tours, best_cost

# Algorithm parameters setup and execution (tuned for simplicity)
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
               (62, 63), (63, 69), (45, 35)]
num_robots = 2
num_iterations = 100
num_ants = 10
alpha = 1.0
beta = 2.0
evaporation_rate = 0.1
initial_pheromone = 0.01

best_tours, best_cost = aco_mTSP(coordinates, num_robots, num_iterations, num_ants, alpha, beta, evaporation_rate, initial_pheromone)

# Output the tour information
for idx, tour in enumerate(best_tours):
    tour_cost = calculate_total_cost([tour], coordinates)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Cost: {best_otp_cost}")