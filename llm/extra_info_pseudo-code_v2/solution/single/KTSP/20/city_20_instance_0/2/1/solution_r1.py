import math
import random
import itertools

# Define the coordinates of each city including the depot city
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
          (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
          (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

def generate_initial_solution():
    selected_cities = random.sample(range(1, 20), 3)
    selected_cities.append(0)  # always include the depot as start and end
    best_route = None
    best_cost = float('inf')
    for perm in itertools.permutations(selected_cities):
        if perm[0] == 0:  # starts at the depot
            route_cost = sum(euclidean_distance(perm[i], perm[i+1]) for i in range(len(perm)-1))
            route_cost += euclidean_distance(perm[-1], 0)  # return to depot cost
            if route_cost < best_cost:
                best_cost = route_cost
                best_route = list(perm)
    return best_route, best_cost

def shake(solution):
    i, j = random.sample(range(1, 4), 2)  # swapping positions within the selected cities, not the depot
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def local_search(solution):
    best_cost = sum(euclidean_distance(solution[i], solution[i+1]) for i in range(len(solution)-1))
    best_cost += euclidean_distance(solution[-1], solution[0])
    for i in range(1, 4):
        for j in range(i + 1, 4):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = sum(euclidean_distance(new_solution[i], new_solution[i+1]) for i in range(len(new_solution)-1))
            new_cost += euclidean_distance(new_solution[-1], new_solution[0])
            if new_cost < best_cost:
                solution, best_cost = new_solution, new_cost
    return solution, best_cost

def gvns():
    best_solution, best_cost = generate_initial_solution()
    iteration = 0
    while iteration < 100:
        current_solution = shake(best_solution[:])
        new_solution, new_cost = local_search(current_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
        iteration += 1
    best_solution.append(best_solution[0]) # return to depot
    return best_solution, best_cost

# Running GVNS algorithm
best_tour, best_tour_cost = gvns()

# Outputting results
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)