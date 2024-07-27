import numpy as np
import random

# City coordinates
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

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return total_distance

# Generate the initial random solution for k cities
def generate_initial_solution(cities, k):
    all_cities = list(cities.keys())
    selected_cities = random.sample(all_cities[1:], k - 1)
    selected_cities = [0] + selected_cities
    random.shuffle(selected_cities[1:])  # Shuffle only non-depot cities
    selected_cities.append(0)  # making it a round trip
    return selected_cities

# Shaking the solution by randomly swapping two cities
def shake(solution):
    new_solution = solution[1:-1]  # Exclude depot city 0 from swapping
    i1, i2 = random.sample(range(len(new_solution)), 2)
    new_solution[i1], new_solut...
    new_solution = [0] + new_solution + [0]
    return new_solution

# Variable Neighborhood Descent exploring N1 (changing one city) and N2 (swapping two cities)
def vnd(solution):
    improved = True
    while improved:
        improved = False
        # N1: Swap one city with another city not in the tour
        for i in range(1, len(solution) - 1):
            for j in range(1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if calculate_total_distance(new_solution) < calculate_total_distance(solution):
                        solution = new_solution
                        improved = True
                        break
            if improved:
                break
    return solution

# Implementing GVNS
def gvns(cities, k, Nrst):
    best_solution = generate_initial_solution(cities, k)
    best_distance = calculate_total_distance(best_solution)
    
    for _ in range(Nrst):
        current_solution = generate_initial_solution(cities, k)
        for _ in range(100):  # Arbitrary number of maximum iterations
            shaken_solution = shake(current_solution)
            improved_solution = vnd(shaken_solution)
            current_distance = calculate_total_distance(improved_solution)
            if current_distance < best_distance:
                best_solution = improved_solution
                best_distance = current_distance
        
    return best_solution, best_distance

# Run the GVNS for 13 cities
tour, total_cost = gvns(cities, 13, 10)
print("Tour:", tour)
print("Total travel cost:", total_cost)