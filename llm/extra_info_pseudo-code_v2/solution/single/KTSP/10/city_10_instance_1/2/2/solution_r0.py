import math
import random

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 13),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def initial_solution(num_cities=5):
    solution = [0]
    remaining_cities = list(cities.keys())[1:]  # Exclude depot
    random.shuffle(remaining_cities)
    solution.extend(remaining_cities[:num_cities-1])
    solution.append(0)  # Return to depot
    return solution

def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def local_search(solution, iterations=100):
    for _ in range(iterations):
        new_solution = solution[:]
        i, j = random.sample(range(1, len(solution) - 1), 2)
        # Swap two cities
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        if total_distance(new_method) < total_distance(solution):
            solution = new_solution
    return solution

def gvns(max_iter=100, num_cities=5):
    best_solution = initial_solution(num_cities)
    best_cost = total_distance(best_solution)
    
    for _ in range(max_iter):
        current_solution = initial_solution(num_cities)
        current_solution = local_search(current_solution)
        current_cost = total_distance(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Execute the GVNS algorithm
best_tour, best_tour_cost = gvns(1000)

# Format output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")