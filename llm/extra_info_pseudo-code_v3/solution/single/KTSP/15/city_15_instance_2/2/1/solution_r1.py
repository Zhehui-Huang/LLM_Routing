import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def generate_initial_solution(cities, k):
    tour = [0]  # Starting at the depot city
    available = list(set(range(1, len(cities))))
    while len(tour) < k - 1:
        next_city = random.choice(available)
        tour.append(next_city)
        available.remove(next_city)
    tour.append(0)  # Return to the depot
    return tour

def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i-1]][tour[i]]
    return total_cost

def shake(tour, k):
    # Make a copy excluding depart and return to modify
    modified_part = tour[1:-1]
    random.shuffle(modified_part)
    new_tour = [0] + modified_part + [0]
    return new_tour

def vnd(tour, distance_matrix, k):
    # Swap adjacent cities (excluding start and end point)
    improved = True
    while improved:
        improved = False
        for i in range(1, k-2):
            new_tour = tour[:]
            new_tour[i], new_tour[i+1] = new_tour[i+1], new_tour[i]  # Swap adjacent cities
            new_cost = calculate_tour_cost(new_tour, distance_matrix)
            if new_cost < calculate_tour_cost(tour, distance_matrix):
                tour = new_tour
                improved = True
    return tour

def gvns(cities, k, Nrst, distance_matrix):
    best_tour = generate_initial_solution(cities, k)
    best_cost = calculate_tour_cost(best_tour, distance_matrix)
    
    for _ in range(Nrst):
        current_tour = shake(best_tour, k)
        current_tour = vnd(current_tour, distance_matrix, k)
        current_cost = calculate_tour_cost(current_tour, distance_matrix)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
    
    return best_tour, best_cost

# Coordinates of cities
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
          (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]
k = 8  # Number of Cities to Visit Including Depot

# Create distance matrix
distance_matrix = construct_distance_matrix(cities)

# Conduct GVNS to find the best tour
best_tour, best_cost = gvns(cities, k, 100, distance_matrix)

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")