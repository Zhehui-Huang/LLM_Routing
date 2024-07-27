import math
import random

# Define the city coordinates with the given environment information
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate total cost of the tour
def evaluate_tour(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Generate an initial solution for the given number of cities to visit
def generate_initial_solution(k, city_count=10):
    included = set([0])
    available_cities = list(set(range(city_count)) - included)
    tour = [0]
    while len(included) < k-1:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        included.add(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Perform local search to improve the solution
def local_search(tour):
    best_cost = evaluate_tour(tour)
    best_tour = tour[:]
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = evaluate_tour(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    made_improvement = True
    return best_tour

# The main GVNS function to find the best solution
def GVNS(k, itermax=100, pmax=5):
    best_solution = generate_initial_solution(k)
    best_cost = evaluate_tour(best_solution)
    iter = 0
    while iter < itermax:
        current_solution = generate_initial_solution(k)
        current_solution = local_search(current_solution)
        current_cost = evaluate_tour(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
        iter += 1
    return best_solution, best_cost

# Run the GVNS function for the problem setup
best_tour, total_cost = GVNS(k=8)

print("Tour:", best_tour)
print("Total travel cost:", total_cost)