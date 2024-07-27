import random
import math

# Define cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Parameters for GVNS
num_itermax = 1000
pmax = 2
k = 10  # Number of cities to visit, including the depot

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def generate_initial_solution():
    solution = [0]  # Start at depot city
    available_cities = list(cities.keys())
    available_cities.remove(0)  # remove depot from available cities
    while len(solution) < k:
        next_city = random.choice(available_cities)
        solution.append(next_city)
        available_cities.remove(next_city)
    solution.append(0)  # End at depot city
    return solution

def local_search(solution, neighborhood):
    best_solution = solution[:]
    best_cost = total_cost(solution)
    improved = False
    
    if neighborhood == 1:
        # neighborhood N1: Exchange operation
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = solution[j], solution[i]
                new_cost = total_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    elif neighborhood == 2:
        # neighborhood N2: All possible 2-opt moves
        for i in range(1, len(solution) - 3):
            for j in range(i + 2, len(solution) - 1):
                new_solution = solution[:i] + solution[i:j+1][::-1] + solution[j+1:]
                new_cost = total_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True

    return best_solution, improved

def vnd(solution):
    p = 1
    improved = True
    while improved:
        solution, improved = local_search(solution, p)
        if improved:
            p = 1
        else:
            p += 1
        if p > pmax:
            break
    return solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_cost(best_solution)

    for _ in range(num_itermax):
        p = 1
        while p <= pmax:
            # Shaking
            current_solution = generate_initial_solution()
            # Variable Neighborhood Descent
            current_solution = vnd(current_solution)
            current_cost = total_cost(current_solution)

            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost
                p = 1  # Restart the shaking process at the first neighborhood
            else:
                p += 1

    return best_solution, best_cost

# Perform the General Variable Neighborhood Search to find the optimal solution
optimal_tour, optimal_cost = gvins()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)