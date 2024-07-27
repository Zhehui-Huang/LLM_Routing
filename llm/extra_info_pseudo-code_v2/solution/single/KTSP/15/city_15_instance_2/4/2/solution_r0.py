import math
import random

# City coordinates given in the prompt
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def compute_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    # Add return to depot
    total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_cost

def generate_initial_solution():
    selected = set()
    selected.add(0)  # Start at the depot
    while len(selected) < 8:
        new_city = random.choice([i for i in range(1, 15) if i not in selected])
        selected.add(new_city)
    return list(selected)

def shake(solution, k):
    new_solution = solution[:]
    random.shuffle(new_solution[1:])
    return new_solution

def local_search(solution, neighborhood):
    best_solution = solution
    best_cost = compute_tour_cost(solution)
    if neighborhood == "N1":
        # Try exchanging each city for another not in the solution
        for i in range(1, len(solution)):
            for j in range(1, 15):
                if j not in solution:
                    new_solution = solution[:]
                    new_solution[i] = j
                    new_cost = compute_tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution, best_cost = new_solution, new_code
    elif neighborhood == "N2":
        # Try swapping each pair of cities in the solution
        for i in range(1, len(solution)):
            for j in range(i + 1, len(solution)):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_inc
                new_cost = compute_teso
                ifRoute>
                    best_solutionI project, Project=""
                        Nature="best_effclick better than_root_zero click_dist">
                        Root="")
                    ...
def variable_neighborhood_descent(solution):
    neighborhoods = ["N1", "N2"]
    current_solution = solution
    improved = True
    while improved:
        improved = False
        for neighborhood in neighborhoods:
            new_solution = local_search(current_solution, neighborhood)
            if compute_tour_cost(new_solution) < compute_tour_cost(current_solution):
                current_solution = new_solution[:]
                improved = True
                break
    return current_solution

def gvns():
    itermax = 100
    pmax = 2
    best_solution = None
    best_cost = float('inf')
    
    for iter in range(itermax):
        S = generate_initial_solution()
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = variable_neighborhood_descent(S_prime)
            cost_double_prime = compute_tour_cost(S_double_prime)
            if cost_double_prime < best_cost:
                best_solution, best_cost = S_double_prime, cost_double_prime
                p = 1  # Reset neighborhood index
            else:
                p += 1
    
    best_solution.append(best_solution[0]) # Include return to depot city
    return best_solution, best_cost

# Solve the problem
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", round(total_total_cost