import math
import random

# Given city coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial solution
def generate_initial_solution(k=12):
    selected_cities = [0]
    available_cities = list(cities.keys())[1:]
    while len(selected_cities) < k:
        city = random.choice(available_cities)
        selected_cities.append(city)
        available_cities.remove(city)
    selected_cities.append(0)  # Closing the tour
    return selected_cities

# Calculate total travel cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Shake the solution (Exchange one city)
def shake(solution):
    new_solution = solution[:-1]  # Remove the last city (duplicate of the first)
    i = random.randint(1, len(new_solution) - 2)
    city_out = new_solution.pop(i)
    city_in = random.choice(list(set(cities.keys()) - set(new_solution)))
    new_solution.insert(random.randint(1, len(new_solution) - 1), city_in)
    new_solution.append(new_solution[0])
    return new_solution

# Local search using swap neighborhoods
def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_cost(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    return best_solution

# GVNS algorithm
def gvns(k=12, max_iter=100):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)

    for _ in range(max_iter):
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    
    return best_solution, best_cost

# Get the solution and print it
best_tour, best_tour_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))