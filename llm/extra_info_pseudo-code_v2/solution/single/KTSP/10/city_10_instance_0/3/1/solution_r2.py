import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_cost(tour, coordinates):
    cost = euclidean_distance(coordinates[tour[-1]], coordinates[tour[0]])  # Closing the tour
    for i in range(len(tour)-1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def generate_initial_solution(coordinates):
    cities = list(range(1, len(coordinates)))  # Avoid the depot (index 0)
    selected_cities = random.sample(cities, 3)
    return [0] + selected_cities + [0]

def shake(solution):
    inner_cities = solution[1:-1]
    random.shuffle(inner_cities)
    return [0] + inner_cities + [0]

def local_search(solution, coordinates):
    best_solution = solution[:]
    best_cost = calculate_cost(solution, coordinates)
    
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution, coordinates)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
    return best_solution

def gvns(coordinates, max_iterations):
    current_solution = generate_initial_solution(coordinates)
    current_cost = calculate_cost(current_solution, coordinates)
    
    for _ in range(max_iterations):
        new_solution = shake(current_solution)
        new_solution = local_search(new_solution, coordinates)
        new_cost = calculate_cost(new_solution, coordinates)
        if new_cost < current_cost:
            current_solution, current_cost = new_solution, new_cost
    return current_solution, current_cost

coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

best_tour, total_cost = gvns(coordinates, 100)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")