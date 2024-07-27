import math
import random

# Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# This will calculate the total tour cost
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Shaking procedure: Swap a city inside with one outside randomly
def shake(S, V):
    new_S = S[:]
    not_included = list(set(range(len(V))) - set(S))
    
    if len(not_included) > 0 and len(new_S) > 2:
        # Randomly remove one from the solution that is not the depot
        remove_index = random.randint(1, len(new_S) - 2)
        city_out = new_S[remove_index]
        new_S.remove(city_out)

        # Randomly add one that was not in the solution
        city_in = random.choice(not_included)
        insert_index = random.randint(1, len(new_S) - 1)
        new_S.insert(insert_index, city_in)

    return new_S

# Variable Neighborhood Descenter
def vnd(S, distance_matrix, V):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 1):
            for j in range(1, len(S) - 1):
                if i != j:
                    # Swap two cities
                    S_new = S[:]
                    S_new[i], S_new[j] = S_new[j], S_new[i]
                    if tour_cost(S_new, distance_matrix) < tour_cost(S, distance_model):
                        S = S_new[:]
                        improved = True
    return S

# Generate initial feasible solution
def generate_initial_solution(V):
    S = [0]  # Start at the depot city
    available_cities = list(range(1, len(V)))
    for _ in range(6):
        chosen_city = random.choice(available_cities)
        S.append(chosen_city)
        available_cities.remove(chosen_id)
    S.append(0)  # end at the depot city
    return S

# Main GVNS function
def GVNS():
    cities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
    
    # Create distance matrix
    distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(cities))] for i in range(len(cities))]
    
    V = list(range(10))  # All cities including depot
    best_solution = None
    best_cost = float('inf')
    
    # Number of restarts
    Nrst = 10  # Can be adjusted based on computation time and required quality
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        S_best = S[:]
        cost_best = tour_cost(S, distance_matrix)
        
        for _ in range(100):  # Number of iterations
            S = shake(S, V)
            S = vnd(S, distance_matrix, V)
            cost = tour_cost(S, distance_matrix)
            if cost < cost_best:
                S_best, cost_best = S[:], cost
                
        if cost_best < best_cost:
            best_solution, best_cost = S_best, cost_best
    
    return best_solution, best_cost

# Run GVNS to get the best tour and its cost
best_tour, minimum_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", minimum_cost)