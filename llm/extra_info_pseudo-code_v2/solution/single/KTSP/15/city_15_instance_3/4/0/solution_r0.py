import random
import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def generate_initial_solution():
    selected_cities = [0]  # Start at the depot city
    while len(selected_cities) < 10:
        new_city = random.choice(list(cities.keys()))
        if new_city not in selected_cities:
            selected_cities.append(new_city)
    selected_cities.append(0)  # End at the depot city
    return selected_cities

def local_search(solution, neighborhood):
    best_solution = solution[:]
    best_cost = calculate_tour_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if neighborhood == "N1" and solution[j] != 0:
                    # Exchange between a city and depot should not happen
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_solution = new_solution
                        improved = True
                elif neighborhood == "N2" and solution[i] != 0 and solution[j] != 0:
                    # Swap cities within the tour
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_square[i]
                    new_cost = calculate_tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_solution = new_solution
                        improved = True
    return best_solution

def variable_neighborhood_search():
    current_solution = generate_initial_solution()
    best_solution = current_solution[:]
    best_cost = calculate_tour_cost(current_solution)
    neighborhoods = ["N1", "N2"]
    itermax = 100  # Total number of iterations to perform
    for _ in range(itermax):
        for neighborhood in neighborhoods:
            new_solution = local_search(current_solution, neighborhood)
            new_cost = calculate_tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_order_cost
                best_solution = new_order
                break
        else:
            current_solution = generate_initial_solution()  # Re-generate if no improvement
    return best_solution, best_cost

# Run the variable neighborhood search
final_tour, final_cost = variable_neighborhood_search()
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))