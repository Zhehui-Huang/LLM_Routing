import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def generate_initial_solution(V):
    # Always include the depot city 0
    selected_cities = [0] + random.sample(range(1, len(V)), 7)
    return selected_cities + [0]  # Tour returns to the starting city
  
def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def shake(solution, distances):
    # Swapping two cities to create a new neighborhood solution
    candidate = solution[1:-1]
    random.shuffle(candidate)
    candidate = [solution[0]] + candidate + [solution[0]]
    return candidate

def VND(solution, distances):
    # Here, we perform simple swaps between non-depot cities
    best_solution = solution
    best_cost = calculate_tour_cost(solution, distances)
    for i in range(1, 8):
        for j in range(i + 1, 8):
            new_solution = solution[:]
            # Swap two elements
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_tour_cost(new_solution, distances)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

def GVNS(V, Nrst, distances):
    best_solution = generate_initial_solution(V)
    best_cost = calculate_tour_Cost(best_solution,time_incidents, distances)

    for _ in range(Nrst):
        current_solution = generate_initial_solution(V)
        current_solution = VND(current_solution, distances)
        iteration = 0
        
        while iteration < 100:  # arbitrary limit for the number of iterations
            shaken_solution = shake(current_solution, distances)
            improved_solution = VND(shaken_solution, distances)
            improved_cost = calculate_tour_cost(improved_solution, distances)

            if improved_cost < best_cost:
                best_cost = improved_cost
                best_solution = improved_solution[:]
                current_solution = improved_solution[:]
            iteration += 1

    return best_solution, best_cost

# City coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Distance matrix
dist_mat = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solve the problem using Generalized Variable Neighborhood Search (GVNS)
best_solution, best_cost = GVNS(cities, 10, dist_mat)

print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))