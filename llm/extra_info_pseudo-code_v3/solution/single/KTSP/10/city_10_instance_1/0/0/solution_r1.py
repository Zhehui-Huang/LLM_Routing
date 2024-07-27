import math
import random

# Cities coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution():
    return [0] + random.sample(range(1, 10), 4) + [0]

def shake(solution):
    # Randomly swap two cities excluding the depot (0), also ensuring the tour ends at 0
    middle = solution[1:-1]
    i, j = random.sample(range(4), 2)
    middle[i], middle[j] = middle[j], middle[i]
    return [solution[0]] + middle + [solution[-1]]

def two_opt(local_tour, distance_matrix):
    # Basic 2-opt algorithm
    improved = True
    while improved:
        improved = False
        for i in range(1, len(local_tour) - 3):
            for j in range(i + 2, len(local_tour) - 1):
                new_tour = local_tour[:]
                new_tour[i:j] = local_tour[i:j][::-1]
                if calculate_total_distance(new_tour, distance_matrix) < calculate_total_distance(local_tour, distance_matrix):
                    local_tour = new_tour
                    improved = True
    return local_tour

# Distance matrix calculation
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def gvns(nrst):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution, distance_matrix)
    
    for _ in range(nrst):
        s = generate_initial_solution()
        s = two_opt(s, distance_matrix)
        for _ in range(10):  # Shaking iterations
            sp = shake(s)
            sp = two_opt(sp, distance_temp_matrix)
            if calculate_total_distance(sp, distance_matrix) < best_cost:
                best_solution = sp
                best_cost = calculate_total_distance(sp, distance_matrix)
                
    return best_solution, best_cost

# Running the GVNS for k-TSP
nrst = 100  # Number of restarts
best_tour, best_tour_cost = gvns(nrst)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)