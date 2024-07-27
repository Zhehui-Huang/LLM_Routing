import random
import math
import itertools

# Define cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# City indices
city_indices = list(cities.keys())

def euclidean_distance(c1, c2):
    """Calculates Euclidean distance between two cities given their indices."""
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def total_distance(tour):
    """Calculates the total Euclidean distance of the tour."""
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """Generates a random initial solution (7 cities including the depot)."""
    selected_cities = random.sample(city_indices[1:], 6)  # select 6 random cities, excluding the depot
    selected_cities.insert(0, 0)  # adding depot at the start
    selected_cities.append(0)  # adding depot at the end
    return selected_cities

def shake(solution):
    """Randomly swap two cities in the solution except the depot."""
    a, b = random.sample(range(1, len(solution) - 1), 2)  # exclude the depot (index 0 and last)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution):
    """Apply simple VND by randomly adjusting the solution and checking for improvements."""
    best_solution = solution[:]
    best_cost = total_distance(best_solution)
    
    for _ in range(20):  # Limit the number of VND iterations for simplicity
        new_solution = shake(best_solution[:])
        new_cost = total_distance(new_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
    return best_solution

def gvns(nr_restarts, max_iter=100):
    best_solution = generate_initial_solution()
    best_cost = total_xinstance(best_solution)

    for _ in range(nr_restarts):
        solution = generate_initial_solution()
        for _ in range(max_iter):
            new_solution = shake(solution[:])
            solution_with_vnd = vnd(new_solution)
            new_cost = total_distance(solution_with_vnd)
            if new_cost < best_cost:
                best_solution, best_cost = solution_with_vnd, new_cost
    
    return best_solution, best_cost

# Run the GVNS algorithm
nr_restarts = 10
solution, cost = gvns(nr_restarts)

# Print the output
print(f"Tour: {solution}")
print(f"Total travel cost: {cost:.2f}")