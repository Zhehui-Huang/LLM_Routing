import numpy as np
import random

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(pos1, pos2):
    return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Pre-compute distances between all cities
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_matrix[i] = {}
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# ACO parameters
ant_count = 10
generations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
pheromone_initial = 1.0

# Initialize pheromones
pheromones = { (i, j): pheromone_initial for i in cities for j in cities if i != j }

def choose_next_city(current_city, visited):
    choices = [(j, pheromones[(current_city, j)] ** alpha * (1/distance_matrix[current_city][j]) ** beta)
               for j in cities if j not in visited]
    total = sum(p[1] for p in choices)
    cummulative = 0
    threshold = random.random()
    for city, prob in choices:
        cummulative += prob / total
        if cummulative >= threshold:
            return city

def ant_colony_optimization():
    best_distance = float('inf')
    best_solution = None

    for generation in range(generations):
        solutions = []
        for ant in range(ant_count):
            solution = []
            visited = set()
            current_city = random.choice(list(cities))
            solution.append(current_city)
            visited.add(current_city)

            while len(visited) < len(cities):
                next_city = choose_next_city(current_city, visited)
                visited.add(next_city)
                solution.append(next_city)
                current_city = next_city

            solution.append(solution[0])  # return to starting depot
            solutions.append(solution)

        # Update pheromones
        for i, j in pheromones:
            pheromones[(i, j)] *= (1 - evaporation_rate)
        
        for solution in solutions:
            distance = sum(distance_matrix[solution[i]][solution[i+1]] for i in range(len(solution) - 1))
            if distance < best_distance:
                best_distance = distance
                best_solution = solution
            for i in range(len(solution)-1):
                pheromones[(solution[i], solution[i+1])] += 1 / distance
                
    return best_solution, best_distance

best_tour, best_tour_cost = ant_colony_optimization()
print(f"Optimal Tour: {best_tour}")
print(f"Optimal Tour Cost: {best_tour_cost:.2f}")