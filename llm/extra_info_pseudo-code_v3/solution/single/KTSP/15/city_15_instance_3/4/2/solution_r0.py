import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def total_tour_distance(cities, tour):
    distance = 0
    for i in range(1, len(tour)):
        distance += distances[tour[i-1]][tour[i]]
    distance += distances[tour[-1]][tour[0]]  # complete the tour back to the depot
    return distance

def generate_initial_solution(city_indices, depot):
    return [depot] + random.sample(city_indices, 9) + [depot]

def shake(solution):
    k = len(solution)
    ind1, ind2 = random.sample(range(1, k-1), 2)  # Don't move the depot
    solution[ind1], solution[ind2] = solution[ind2], solution[ind1]
    return solution

def vnd(solution):
    improved = True
    while improved:
        improved = False
        # Scan all possible 2-swap neighborhoods
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if total_tour_distance(cities, new_solution) < total_tour_distance(cities, solution):
                    solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return solution

def variable_neighborhood_search(cities, distances, num_restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution(range(1, len(cities)), 0)
        while True:
            new_solution = shake(current_solution[:])
            new_solution = vnd(new_solution)
            new_cost = total_tour_distance(cities, new_solution)
            current_cost = total_tour_distance(cities, current_solution)
            
            if new_cost < current_cost:
                current_solution = new_solution
            else:
                break
        
        if new_cost < best_cost:
            best_solution = current_solution
            best_cost = new_cost
    
    return best_solution, best_cost

# Define city coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Run the variable neighborhood search algorithm
best_tour, best_cost = variable_neighborhood_search(cities, distances, 100)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))