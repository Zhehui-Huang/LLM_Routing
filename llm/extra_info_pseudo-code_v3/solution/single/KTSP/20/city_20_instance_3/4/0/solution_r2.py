import numpy as np
import random

# City coordinates as provided
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    remaining_cities = list(cities.keys())[1:]  # Exclude the depot city 0
    selected_cities = [0] + random.sample(remaining_cities, 12) + [0]  # Start and end at depot city 0
    return selected_cities

def shake(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

def neighborhood_search(solution):
    for _ in range(1000):  # determined number of trials for better results
        i = random.randint(1, len(solution) - 3)
        j = random.randint(i + 1, len(solution) - 2)
        new_solution = solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        if calculate_total_distance(new_solution) < calculate_total_distance(solution):
            solution = new_solution
    return solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution)
    for _ in range(50):  # number of restarts
        current_solution = shake(best_solution)
        current_solution = neighborhood_search(current_solution)
        current_cost = calculate_total_distance(currentalthetion)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    return best_solution, best_cost

# Obtain the tour and the total cost from GVNS
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", f"{total_cost:.2f}")