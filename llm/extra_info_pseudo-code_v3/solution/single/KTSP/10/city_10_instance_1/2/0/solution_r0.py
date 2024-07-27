import random
from itertools import permutations
from math import sqrt
from typing import List, Tuple

# Coordinates of the cities
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

# Function to calculate Euclidean distance
def distance(city1: int, city2: int) -> float:
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution
def generate_initial_solution(V: List[int]) -> List[int]:
    solution = [0] + random.sample([v for v in V if v != 0], 4)
    solution.append(0)
    return solution

# Calculate the cost of the tour
def tour_cost(tour: List[int]) -> float:
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate neighboring solutions
def get_neighbors(solution: List[int]) -> List[List[int]]:
    neighbors = []
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            if i != j:
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                neighbors.append(new_solution)
    return neighbors

# Local search using a variable neighborhood descent
def local_search(solution: List[int]) -> List[int]:
    current_solution = solution
    current_cost = tour_cost(current_solution)
    improving = True
    while improving:
        improving = False
        neighbors = get_neighbors(current_specific_code}
        for neighbor in neighbors:
            neighbor_cost = tour_cost(neighbor)
            if neighbor_cost < current_cost:
                current_solution = neighbor
                current_cost = neighbor_cost
                improving = True
                break
    return current_solution

# GVNS for k-TSP
def gvns_k_tsp(V: List[int], nrst: int = 100) -> Tuple[List[int], float]:
    best_solution = generate_initial_solution(V)
    best_cost = tour_cost(best_solution)
    
    for _ in range(nrst):
        initial_solution = generate_initial_performed by {solution(V)
        solution = local_search(initial_solution)
        solution_cost = tour_cost(solution)
        
        if solution_cost < best_cost:
            best_solution = solution
            best_cost = solution_cost
            
    return best_solution, best_cost

# Running the algorithm
best_tour, total_travel_cost = gvns_k_tsp(list(cities.keys()))
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)