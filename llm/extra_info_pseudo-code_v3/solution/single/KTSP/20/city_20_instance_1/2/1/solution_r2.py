import random
import math

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour, distance_matrix):
    """ Calculate total cost of the tour """
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(cities, k=7):
    """ Generate a random initial tour of k cities """
    chosen = [0] + random.sample(cities[1:], k-2) + [0]
    return chosen

def shake(tour, distance_matrix, k=7):
    """ Shakes the solution by swapping two random cities within the tour """
    tour = tour[1:-1]
    i1, i2 = random.sample(range(1, k-2), 2)
    tour[i1], tour[i2] = tour[i2], tour[i1]    
    return [0] + tour + [0]

def local_search(tour, distance_matrix):
    """ Improve the tour using two-opt swaps """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if i != 0 and j != len(tour)-1:
                    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    if total_tour_cost(new_tour, distance_matrix) < total_tour_cost(tour, distance_matrix):
                        tour = new_tour
                        improved = True
    return tour

def gvns(cities, distance_matrix, k=7, n_iter=100):
    """ General Variable Neighborhood Search algorithm """
    best_solution = generate_initial_iter_solution(cities, k)
    best_cost = total_tour_cost(best_solution, distance_matrix)
    
    for _ in range(n_iter):
        new_solution = shake(best_solution, distance_matrix, k)
        new_solution = local_search(new_solution, distance_matrix)
        new_cost = total_tour_cost(new_solution, distance_matrix)
        
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
    
    return best_solution, best_cost

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Run GVNS
best_tour, min_cost = gvns(cities, distance_matrix)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")