import numpy as np
import math

# City coordinates and robot information:
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
# Each depot is associated with a specific robot starting and ending there
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = 8

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize pheromones and heuristic information
num_cities = len(cities)
pheromones = np.ones((num_cities, num_cities))
heuristic = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            heuristic[i, j] = 1 / euclidean_distance(i, j)

# ACO parameters
num_ants = num_robots
alpha = 1.0  # influence of pheromone
beta = 2.0   # influence of heuristic
evaporation_rate = 0.5
iterations = 100

# Generate tours
def generate_tour(depot):
    tour = [depot]
    visited = set(tour)
    current = depot
    
    while len(visited) < num_cities:
        probabilities = []
        for j in range(num_cities):
            if j not in visited:
                prob = (pheromones[current][j] ** alpha) * (heuristic[current][j] ** beta)
                probabilities.append((j, prob))
        
        if probabilities:
            next_city = max(probabilities, key=lambda x: x[1])[0]
            tour.append(next_city)
            visited.add(next_city)
            current = next_city
    
    tour.append(depot)  # return to depot
    return tour

# Calculate the total cost of a tour
def calculate_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    return cost

# Main ACO loop
best_tours = None
best_total_cost = float('inf')

for iteration in range(iterations):
    tours = []
    total_cost = 0
    
    for robot in range(num_robots):
        depot = depots[robot]
        tour = generate_tour(depot)
        tours.append(tour)
        cost = calculate_cost(tour)
        total_cost += cost
        
        for i in range(1, len(tour)):
            pheromones[tour[i-1]][tour[i]] *= (1 - evaporation_rate)
            pheromones[tour[i-1]][tour[i]] += 1 / cost  # global updating
    
    if total_cost < best_total_cost:
        best_total_cost = total_cost
        best_tours = tours

# Output the results
for i, tour in enumerate(best_tours):
    tour_cost = calculate_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(best_total_cost, 2)}")