import math
import random

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, home_city):
    other_cities = list(cities.keys())
    other_cities.remove(home_city)
    random.shuffle(other_cities)
    return [home_city] + other_cities[:4] + [home_city]

def shake(solution, k):
    # Choose k random indices to swap (not including the first and last which are the depot)
    indices = random.sample(range(1, len(solution) - 1), k)
    solution[indices[0]], solution[indices[1]] = solution[indices[1]], solution[indices[0]]
    return solution

def vnd(solution, neighborhoods, distance_matrix):
    for nh in neighborhoods:
        improved = True
        while improved:
            improved = False
            if nh == "N1":
                for i in range(1, len(solution) - 2):
                    for j in range(i + 1, len(solution) - 1):
                        new_solution = solution[:]
                        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                        if total_tour_distance(new_solution, distance_matrix) < total_tour_distance(solution, distance_matrix):
                            solution = new_solution
                            improved = True
                            break
                    if improved:
                        break
    return solution

def gvns(cities, distance_matrix, nrst=100, max_iterations=100):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, 0)
        current_cost = total_tour_distance(current_solution, distance_matrix)
        iteration = 0
        
        while iteration < max_iterations:
            k = 2  # Shaking strength
            new_solution = shake(current_solution.copy(), k)
            improved_solution = vnd(new_solution, ["N1"], distance_matrix)
            improved_cost = total_tour_distance(improved_solution, distance_matrix)
            
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
                iteration = 0  # Reset on improvement
            else:
                iteration += 1
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Input cities as coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Creating distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = eu waiver_distance(*cities[i], *cities[j])

# Find the best path using GVNS
best_tour, best_cost = gvns(cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost))