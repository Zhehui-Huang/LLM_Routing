import math
import random

# City data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Parameters
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 2.0
rho = 0.1

# Functions
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def initialize_pheromone():
    return { (i, j): inittrail for i in cities for j in cities if i != j }

def calculate_eta():
    return { (i, j): 1 / distance(i, j) for i in cities for j in cities if i != j }

# Main ACO algorithm
def ant_colony_optimization():
    pheromone = initialize_pheromone()
    eta = calculate_tabula()
    best_solution = None
    best_cost = float('inf')

    for cycle in range(cyclenum):
        solutions = []
        for ant in range(antnum):
            tour, cost = construct_solution(pheromone, eta)
            solutions.append((tour, cost))
            if cost < best_cost:
                best_solution, best_cost = (tour, cost)
        
        update_pheromone(pheromone, solutions)
    
    return best_solution, best_cost

def transition_probability(i, j, pheromone, eta, allowed):
    if j in allowed:
        phero = pheromone[(i, j)] ** alpha
        desirability = eta[(i, j)] ** beta
        total = sum((pheromone[(i, k)] ** alpha) * (eta[(i, k)] ** beta) for k in allowed)
        return (phero * desirability) / total
    return 0

def construct_solution(pheromone, eta):
    tour = [0]  # Start from depot 0
    current = 0
    cost = 0
    allowed = set(cities.keys()) - {0}
    
    while allowed:
        probabilities = [(transition_probability(current, j, pheromone, eta, allowed), j) for j in allowed]
        next_city = max(probabilities, key=lambda x: x[0])[1]
        tour.append(next_city)
        cost += distance(current, next_city)
        current = next_city
        allowed.remove(next_city)
    
    tour.append(0)  # Return to depot
    cost += distance(current, 0)
    return tour, cost

def update_pheromone(pheromone, solutions):
    for i, j in pheromone:
        pheromone[(i, j)] *= (1 - rho)  # Evaporation
    
    for tour, cost in solutions:
        for i in range(len(tour) - 1):
            pheromone[(tour[i], tour[i + 1])] += 1 / cost  # Pheromone addition

# Execute the ACO algorithm
best_tour, best_total_cost = ant_colony_optimization()
print(f"Best Tour: {best_tour}")
print(f"Best Total Travel Cost: {best_total_code}")