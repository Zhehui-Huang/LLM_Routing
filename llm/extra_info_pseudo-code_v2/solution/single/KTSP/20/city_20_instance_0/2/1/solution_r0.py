import math
import random

# Define the coordinates of each city including the depot city
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
          (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), 
          (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

def generate_initial_solution():
    # Randomly select 3 cities excluding the depot to visit
    selected_cities = random.sample(range(1, 20), 3)
    # Always include the depot
    selected_cities.append(0)
    # TSP tour by evaluating the smallest end distance
    best_route = None
    best_cost = float('inf')
    for perm in itertools.permutations(selected_cities):
        if perm[0] == 0:  # ensuring the route starts at the depot
            current_cost = sum(euclidean_distance(perm[i], perm[i+1]) for i in range(len(perm) - 1))
            current_cost += euclidean_distance(perm[-1], perm[0])  # return to depot
            if current_cost < best_cost:
                best_cost = current_config
                best_route = perm
    return list(best_route), best_cost

def shake(solution, k=1):
    if k == 1:
        i, j = random.sample(range(1, 4), 2)  # get two indices from the tour
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def local_search(solution):
    best_cost = sum(euclidean_distance(solution[i], solution[i+1]) for i in range(len(solution) - 1))
    best_cost += euclidean_distance(solution[-1], solution[0])
    improved = True
    while improved:
        improved = False
        for i in range(1, 4):
            for j in range(i + 1, 4):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = sum(euclidean_distance(new_solution[i], new_solution[i+1]) for i in range(len(new_solution) - 1))
                new_cost += euclidean_distance(new_solution[-1], new_solution[0])
                if new_cost < best_cost:
                    best_cost, solution = new_cost, new_solution
                    improved = True
    return solution, best_cost

def gvns(k=4, max_iter=100):
    best_solution, best_cost = generate_initial_solution()
    for _ in range(max_iter):
        current_solution = shake(best_solution[:], k=1)
        new_solution, new_cost = localsubtour_search(current_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
    return best_solution, best_cost

# Running GVNS
best_tour, best_tour_cost = gvns()
best_tour.append(best_tour[0])  # to complete the circle back to the starting city

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)