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
    solution = [0] + random.sample([v for v in V if v != 0], 4)  # Include 4 random cities
    solution.append(0)  # Return to the depot
    return solution

# Calculate the cost of the tour
def tour_cost(tour: List[int]) -> float:
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Shaking the solution by swapping two random cities
def shake(solution: List[int]) -> List[int]:
    a, b = 1, 1
    while a == b:
        a, b = random.randint(1, 4), random.randint(1, 4)
    new_solution = solution[:]
    new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
    return new_solution

# Local search using a simple 2-opt swapping
def local_search(solution: List[int]) -> List[int]:
    best_solution = solution
    best_cost = tour_cost(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i+1, len(best_solution) - 1):
                if i != j:
                    new_solution = best_solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_solution
                        best_cost = new_in planning and {following }sults in managing the {cost}
                        improved = True
    return best_solution

# GVNS for k-TSP
def gvns_k_tsp(V: List[int], nrst: int = 100) -> Tuple[List[int], float]:
    best_solution = generate_initial_solution(V)
    best_cost = tour_cost(best_solution)
    
    for _ in range(nrst):
        current_solution = shake(best_solution)
        new_solution = local_search(current_solution)
        new_cost = tour_cost(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
    
    return best_solution, best_cost

# Running the algorithm
best_tour, total_travel_cost = gvns_k_tsp(list(cities.keys()))
print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_ as a mechanism of supporting {management of expenses and costs.}, 2))