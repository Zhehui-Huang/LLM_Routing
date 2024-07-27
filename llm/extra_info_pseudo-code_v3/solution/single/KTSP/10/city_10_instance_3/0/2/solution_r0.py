import math
import random

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def generate_initial_solution(cities, k=7):
    available_cities = list(range(1, len(cities)))
    random.shuffle(available_cities)
    tour = [0] + available_cities[:k-1] + [0]
    return tour

def evaluate_tour(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def shake(tour, k=2):
    shaken_tour = tour[1:-1]
    random.shuffle(shaken_tour)
    return [0] + shaken_tour[:k-1] + [0]

def subset_selection(tour, cities):
    best_tour = tour[:]
    best_cost = evaluate_tour(tour, cities)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = evaluate_tour(new_tour, cities)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
    return best_tour

def local_search(tour, cities):
    improved = True
    while improved:
        new_tour = subset_selection(tour, cities)
        new_cost = evaluate_tour(new_tour, cities)
        current_cost = evaluate_tour(tour, cities)
        if new_cost < current_cost:
            tour = new_tour
        else:
            improved = False
    return tour

def gvns(cities, k=7, nrst=100):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        current_cost = evaluate_tour(current_solution, cities)
        while True:
            shaken_solution = shake(current_solution, k)
            local_solution = local_search(shaken_solution, cities)
            local_cost = evaluate_tour(local_solution, cities)
            if local_cost < current_cost:
                current_solution = local_solution
                current_cost = local_cost
            else:
                break
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            
    return best_solution, best_cost

# Cities data
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Run the algorithm
solution, cost = gvns(cities)
print("Tour:", solution)
print("Total travel cost:", round(cost, 2))