import math
import random

# City coordinates, including depot as index 0
city_coords = [
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Constants and Parameters
k = 8  # Number of Cities to visit, including the depot
itermax = 100  # Maximum number of iterations
pmax = 3  # Number of neighborhoods

def euclidean_distance(pt1, pt2):
    return math.hypot(pt1[0] - pt2[0], pt1[1] - pt2[1])

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return total_cost

def generate_initial_solution():
    cities = list(range(1, len(city_coords)))  # Skip the depot initially
    random.shuffle(cities)
    tour = [0] + cities[:k-1] + [0]
    return tour

def shake(solution, k):
    # Slight perturbation: perform k random swaps inside the tour
    tour = solution[1:-1]
    for _ in range(k):
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return [0] + tour + [0]

def local_search(tour):
    # Local search by swapping two cities
    min_cost = calculate_tour_cost(tour)
    best_tour = tour.copy()
    n = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                new_tour = tour[:i] + [tour[j]] + tour[i+1:j] + [tour[i]] + tour[j+old]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < min_cost:
                    min_cost = new_cost
                    best_tour = new_tour.copy()
                    improved = True
                    break
            if improved:
                break
    return best_tour

def vnd(solution):
    # Various Neighborhood Descent requires multiple neighborhood structures
    return local_search(solution)

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    iter = 0
    
    while iter < itermax:
        current_solution = shake(best_solution, k)
        new_solution = vnd(current_solution)
        new_cost = calculate_tour_cost(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
        
        iter += 1
    
    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, tour_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", tour_cost)