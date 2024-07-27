import numpy as np
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49),   3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41),   8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Distance function (Euclidean)
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize pheromone levels
num_cities = len(cities)
pheromone = np.ones((num_cities, num_cities))
visibility = 1 / np.array([[distance(i, j) if i != j else 1e-10 for j in range(num_cities)] for i in range(num_cities)])

# Ant Colony Optimization parameters
num_ants = 8
iterations = 100
alpha = 1.0   # Phreromone importance
beta = 5.0    # Distance priority
evaporation = 0.5
pheromone_deposit = 1.0

# Robots start and end cities (depots)
robot_depots = list(range(8))

# Main ACO Function
def ACO():
    best_cost = float('inf')
    best_solution = []
    
    for iteration in range(iterations):
        all_routes = []
        for ant in range(num_ants):
            current_city = robot_depots[ant]
            tour = [current_city]
            remaining = set(cities.keys()) - {current_city}

            while remaining:
                probabilities = [(pheromone[current_city][next_city]**alpha) * (visibility[current_city][next_city]**beta)
                                 for next_city in remaining]
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(list(remaining), p=probabilities)
                tour.append(next_socket)
                current_city = next_socket
                remaining.remove(next_socket)

            tour.append(tour[0])  # return to start
            all_routes.append(tour)

        total_cost = 0
        for tour in all_routes:
            tour_cost = sum([distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)])
            total_cost += tour_cost
            
            # Update pheromone (deposit)
            for i in range(len(tour) - 1):
                pheromone[tour[i]][tour[i+1]] += pheromone_deposit / tour_cost
        
        # Update pheromone (evaporation)
        pheromone *= (1 - evaporation)

        # Check if this solution is the best found so far
        if total_cost < best_cost:
            best_cost = total_cost
            best_solution = all_routes

    return best_solution, best_cost

# Run the ACO algorithm
solution, overall_cost = ACO()

# Output the results
def display_results(solution, overall_cost):
    for i, tour in enumerate(solution):
        print(f"Robot {i} Tour: {tour}")
        tour_cost = sum([distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)])
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

display_results(solution, overall_cost)