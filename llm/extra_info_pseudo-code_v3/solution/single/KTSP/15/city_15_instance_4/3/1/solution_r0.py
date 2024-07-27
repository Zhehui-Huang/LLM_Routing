import random
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(*coordinates[tour[i]], *coordinates[tour[i + 1]])
    return total_distance

def shake(solution):
    new_solution = solution[:]
    idx1, idx2 = sorted(random.sample(range(1, len(solution) - 1), 2))
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

def vnd(solution, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution, coordinates) < calculate_total_distance(solution, coordinates):
                    solution = new_solution[:]
                    improved = True
    return solution

def generate_initial_solution(total_cities, depot, city_count):
    solution = [depot] + random.sample(range(1, total_cities), city_count - 1) + [depot]
    return solution

def gvns(start_city, total_cities, city_count, coordinates, n_restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(n_restarts):
        current_solution = generate_initial_solution(total_cities, start_city, city_count)
        current_cost = calculate_total_distance(current_solution, coordinates)
        local_optimum = False
        
        while not local_optimum:
            new_solution = shake(current_solution)
            improved_solution = vnd(new_solution, coordinates)

            improved_cost = calculate_total_distance(improved_solution, coordinates)
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
            else:
                local_optimum = True
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# Constants and Inputs
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
               (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
               (53, 80), (21, 21), (12, 39)]
total_cities = 15

# Run GVNS Algorithm
best_tour, best_tour_cost = gvns(start_city=0, total_cities=total_cities, city_count=12, coordinates=coordinates, n_restarts=100)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)