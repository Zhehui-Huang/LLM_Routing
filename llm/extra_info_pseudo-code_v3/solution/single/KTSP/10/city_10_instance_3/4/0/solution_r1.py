import math
import random

# Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# This will calculate the total tour cost
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Heat function: improves the current solution by swapping possible pairs
def heat(S, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                if i != j:
                    S_new = S[:]
                    S_new[i], S_new[j] = S_new[j], S_new[i]  # Swap two cities
                    if tour_cost(S_new, distance_matrix) < tour_cost(S, distance_matrix):
                        S = S_new[:]
                        improved = True
    return S

# Shaking procedure: Swap a city inside with one outside randomly
def shake(S, V, k):
    new_S = S[:]
    not_included = list(set(V) - set(S))
    
    if len(not_included) > 0:
        # Randomly swap one from the tour with one not in the tour
        for _ in range(k):
            if len(new_S) > 2:
                remove_index = random.randint(1, len(new_S) - 2)
                city_out = new_S.pop(remove_index)
                city_in = random.choice(not_included)
                new_S.insert(random.randint(1, len(new_S) - 1), city_in)
                not_included.append(city_out)
                not_included.remove(city_in)
    return new_S

# Generate initial feasible solution
def generate_initial_solution(V, k):
    S = [0]  # Start at the depot
    chosen_cities = random.sample(V[1:], k-2)  # Choose k-2 cities randomly (not including the depot)
    S += chosen_cities
    S.append(0)  # End at the depot
    return S

# Main GVNS function
def GVNS(V, coordinates, k, Nrst, iterations):
    # Create distance matrix
    distance_matrix = [[calculate_snapshot_distance(coordinates[i], coordinates[j]) for j in V] for i in V]
    
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        S = generate_initial_solution(V, k)
        S_best = S[:]
        cost_best = tour_cost(S, distance_matrix)
        
        for _ in range(iterations):
            S = shake(S, V, max(1, k//10))
            S = heat(S, distance_matrix)
            cost = tour_cost(S, distance_matrix)
            if cost < cost_best:
                S_best, cost_best = S[:], cost
            
        if cost_best < best_cost:
            best_solution, best_cost = S_best, cost_best
    
    return best_solution, best_cost

# Define the problem
V = list(range(10))  # All cities indexed from 0 to 9
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Including the depot
Nrst = 10  # Number of restarts
iterations = 100  # Iterations per restart

# Execute GVNS to find the best tour and cost
best_tour, minimum_cost = GVNS(V, coordinates, k, Nrst, iterations)
print("Tour:", best_tour)
print("Total travel cost:", round(minimum_cost, 2))