import math
import random

# Define the cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def generate_initial_solution():
    selected_cities = [0]
    while len(selected_cities) < 13:
        new_city = random.choice(list(cities.keys()))
        if new_city not in selected_cities:
            selected_cities.append(new_city)
    selected_cities.append(0)  # Return to the depot city
    return selected_cities

def shake(solution, k):
    if k == 1:
        i, j = random.sample(range(1, 12), 2)  # choose two indices to swap, not including the depot city
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def local_search(solution):
    best_solution = solution[:]
    best_distance = calculate_total_distance(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution)
                if new_distance < best_distance:
                    best_solution = new_solution[:]
                    best_distance = new_distance
                    improved = True
    return best_solution

def gvns():
    itermax = 100
    pmax = 10
    best_solution = None
    best_distance = float('inf')

    for _ in range(itermax):
        solution = generate_initial_solution()
        p = 1
        while p <= pmax:
            current_solution = shake(solution, p)
            new_solution = local_search(current_solution)
            new_distance = calculate_total_distance(new_solution)
            if new_distance < best_distance:
                best_solution = new_solution[:]
                best_distance = new_distance
                p = 1  # reset p if improvement is found
            else:
                p += 1
    return best_solution, best_distance

# Run the GVNS algorithm
best_solution, best_distance = gvns()

# Print the results
print("Tour:", best_solution)
print("Total travel cost:", best_distance)