import random
import math

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def get_distance_matrix(cities):
    n = len(cities)
    D = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            D[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return D

def generate_initial_solution(num_cities, tour_length=7):
    tour = [0] + random.sample(range(1, num_cities), tour_length - 2) + [0]
    return tour

def calculate_tour_cost(tour, D):
    return sum(D[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def local_search(tour, D):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour, D)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                new_cost = calculate_tour_cost(new_tour, D)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improved = True
    return best_tour

def GVNS(cities, num_iterations=1000, tour_length=7):
    num_cities = len(cities)
    D = get_distance_matrix(cities)
    best_solution = generate_initial_solution(num_cities, tour_length)
    best_cost = calculate_tour_cost(best_solution, D)

    for _ in range(num_iterations):
        current_solution = generate_initial_solution(num_cities, tour_length)
        current_solution = local_search(current_solution, D)
        current_cost = calculate_tour_cost(current_solution, D)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution[:], current_cost

    return best_solution, best_cost

# Execute the algorithm
best_tour, total_cost = GVNS(cities, 1000)

# Output the solution
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")