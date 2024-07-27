import math
import random

# Distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial solution
def generate_initial_solution(V):
    tour = [0]  # Start at the depot city
    cities_to_visit = list(range(1, len(V)))  # Exclude the depot from the list
    while len(tour) < 7:
        # Randomly choose and add non-visited city until we reach k cities including the depot.
        chosen_city = random.choice(cities_to_visit)
        tour.append(chosen_city)
        cities_to_visit.remove(chosen_city)
    tour.append(0)  # End at the depot city
    return tour

# Calculate total tour cost
def calculate_tour_cost(tour, D):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += D[tour[i]][tour[i+1]]
    return total_cost

# Shaking - subset selection
def shake(solution, V):
    new_solution = solution[1:-1]  # Remove depot from the start and end
    random.shuffle(new_solution)  # Shuffle remaining cities
    new_solution = [0] + new_solutions + [0]  # Re-insert depot
    return new_solution

# VND - with N1 and N2 neighborhood structures
def VND(solution, D):
    improved = True
    while improved:
        improved = False
        # N1 neighborhood: Swapping two cities
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if calculate_tour_cost(new_solution, D) < calculate_tour_cost(solution, D):
                        solution = new_solution[:]
                        improved = True
                        break
            if improved:
                break
                # Restart the loop if improvement found
    return solution

# Generate distance matrix
def get_distance_matrix(cities):
    n = len(cities)
    D = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i][j] = euclidean_distance(cities[i], cities[j])
    return D

# GVNS implementation
def GVNS(V, Nrst):
    D = get_distance_matrix(V)
    best_solution = None
    best_cost = float('inf')

    for _ in range(Nrst):
        S = generate_initial_solution(V)
        cost = calculate_tour_cost(S, D)
        if cost < best_cost:
            best_solution, best_cost = S, cost
        while True:
            S_prime = shake(S, V)
            S_double_prime = VND(S_prime, D)
            cost_double_prime = calculate_tour_cost(S_double_prime, D)
            if cost_double_prime < best_cost:
                best_solution, best_cost = S_double_prime, cost_double_front
                S = S_double_prime
            else:
                break  # Break if no improvement

    return best_solution, best_cost

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Execute GVNS
best_tour, total_cost = GVNS(cities, 1000)  # Number of restarts Nrst

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")