import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def generate_initial_solution(cities, num_cities=16):
    selected = [0] + random.sample(cities[1:], num_cities - 1)
    selected += [0]  # Complete the tour by returning to the depot
    return selected

def shake(solution):
    n = len(solution) - 2  # Exclude the first and last because they are the depot
    i, j = random.sample(range(1, n), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def vnd(solution, coordinates):
    best_cost = total_tour_cost(solution, coordinates)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_tour_cost(new_solution, coordinates)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    return best_solution

def gvns(coordinates, num_restarts=100, num_cities=16):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        solution = generate_initial_solution(range(len(coordinates)), num_cities)
        solution = vnd(solution, coordinates)
        cost = total_tour_cost(solution, coordinates)
        
        if cost < best_cost:
            best_cost = cost
            best_solution = solution
        
        # Conducting shaking and further VND
        for _ in range(5):  # Limited shaking attempts
            shaken_solution = shake(solution[:])
            shaken_solution = vnd(shaken_solution, coordinates)
            shaken_cost = total_tour_cost(shaken_solution, coordinates)
            if shaken_cost < best_cost:
                best_cost = shaken_cost
                best_solution = shaken_solution
        
    return best_solution, best_cost

# Coordinates of the cities (indexed from 0 to 19)
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

best_tour, best_cost = gvns(coordinates)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)