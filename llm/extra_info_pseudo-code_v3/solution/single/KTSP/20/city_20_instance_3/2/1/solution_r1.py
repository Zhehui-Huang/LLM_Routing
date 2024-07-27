import random
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    selected_cities = random.sample(cities[1:], k-1)  # Sample k-1 cities excluding the depot
    return [0] + selected_cities + [0]

def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [solution[0]] + new_solution + [solution[-1]]

def local_search(solution, distance_matrix):
    best_solution = solution[:]
    best_cost = calculate_total_distance(solution, distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_distance(new_solution, distance_matrix)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
                    improved = True
    return best_solution

def gvns(k, cities, distance_matrix, nrst, max_iterations):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        current_cost = calculate_total_distance(current_solution, distance_matrix)
        iteration = 0
        while iteration < max_iterations:
            new_solution = shake(current_solution)
            improved_solution = local_search(new_solution, distance_matrix)
            new_cost = calculate_total_distance(improved_solution, distance_matrix)
            
            if new_cost < current_cost:
                current_solution = improved_solution[:]
                current_cost = new_cost
                iteration = 0  # Reset iteration count on improvement
            else:
                iteration += 1
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Define cities based on the given coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Generate distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solve using GVNS
k = 13
nrst = 10
max_iterations = 100
best_tour, best_cost = gvns(k, list(range(len(cities))), distance_matrix, nrst, max_iterations)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))