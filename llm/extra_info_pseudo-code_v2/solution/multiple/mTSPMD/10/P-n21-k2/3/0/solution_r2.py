import numpy as np
import random

# Define city coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
])

def euclidean_distance(pos1, pos2):
    return np.linalg.norm(np.array(pos1) - np.array(pos2))

# Initialize the distances and pheromone levels
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = distance_matrix[j, i] = euclidean_distance(coordinates[i], coordinates[j])

def aco_solve(num_robots=2, alpha=1.0, beta=2.0, rho=0.1, init_pheromone=1.0, ant_count=50, iterations=100):
    pheromone = np.full((num_cities, num_cities), init_pheromone)
    best_distance = np.inf
    best_solution = None

    for _ in range(iterations):
        all_tours = []
        for ant in range(ant_count):
            tours = []
            costs = []
            available_cities = set(range(num_cities))
            for robot in range(num_robots):
                depot = robot  # Robot 0 starts/ends at city 0, Robot 1 starts/ends at city 1
                tour = [depot]
                current_city = depot
                available_cities.remove(current_city)
                
                while available_cities:
                    next_city = choose_next_city(current_city, available_cities, pheromone, distance_matrix, alpha, beta)
                    if next_city is None:
                        break
                    tour.append(next_city)
                    current_city = next_city
                    available_cities.remove(current_city)
                
                tour.append(depot)
                tours.append(tour)
                costs.append(calculate_tour_cost(tour, distance_matrix))
            
            all_tours.append((tours, sum(costs)))

        # Update pheromones
        pheromone *= (1 - rho)
        for tours, _ in all_tours:
            for tour in tours:
                for i in range(len(tour) - 1):
                    pheromone[tour[i], tour[i+1]] += 1 / calculate_tour_cost(tour, distance_matrix)

        # Store the best found solution
        for tours, cost in all_tours:
            if cost < best_distance:
                best_distance = cost
                best_solution = tours

    return best_solution, best_distance

def choose_next_city(current_city, available_cities, pheromone, distance_matrix, alpha, beta):
    if not available_cities:
        return None
    choices = list(available_cities)
    probs = [pheromone[current_city][next_city] ** alpha * (1 / distance_matrix[current_city][next_city]) ** beta for next_city in choices]
    probs = probs / np.sum(probs)
    return np.random.choice(choices, p=probs)

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Find best solution using ACO
best_solution, best_cost = aco_solve()
print(f"Best Tours by Robots: {best_solution}")
print(f"Minimum Cost Achieved: {best_cost}")