import random
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Distance matrix computation
def compute_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                distance_matrix[i][j] = euclidean_distance(x1, y1, x2, y2)
            else:
                distance_matrix[i][j] = 0
    return distance_matrix

# Simulated Annealing Algo
def simulated_annealing(cities, initial_temperature, cooling_rate):
    current_solution = list(cities.keys())
    random.shuffle(current_solution)
    current_solution.append(current_solution[0]) # close the loop
    current_cost = path_cost(current_solution, cities)
    
    temperature = initial_temperature
    while temperature > 1:
        new_solution = current_solution[:]
        l = random.randint(1, len(cities) - 2)
        k = random.randint(1, len(cities) - 2)        
        new_solution[l], new_solution[k] = new_solution[k], new_solution[l] # swap two cities
        new_cost = path_cost(new_solution, cities)
        
        # Acceptance probability (Metropolis criterion)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = newity_cost
        
        temperature *= cooling_rate

    return current_solution, current_cost

def path_cost(solution, cities):
    cost = 0
    for i in range(1, len(solution)):
        cost += cities[solution[i-1]][solution[i]]
    return cost

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30), 
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79), 
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Generate distance matrix
distance_matrix = compute_distance_matrix(cities)

# Solve TSP
tour, cost = simulated_annealing(distance_matrix, 10000, 0.995)

# Show the resulting tour and the total cost
print("Tour:", tour)
print("Total travel cost:", cost)