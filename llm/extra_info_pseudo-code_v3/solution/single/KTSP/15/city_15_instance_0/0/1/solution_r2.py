import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(V, k):
    # Start with the depot, add k-1 more random cities, and return to depot
    cities = list(range(1, len(V)))
    random.shuffle(cities)
    return [0] + cities[:k-1] + [0]

def shake(S, V, k):
    # Select a non-depot city in the tour randomly and replace it with an unvisited city
    current_cities = S[1:-1]
    available_cities = list(set(range(1, len(V))) - set(current_cities))
    city_to_replace = random.choice(current_cities)
    new_city = random.choice(available_cities)
    # Replace in the tour
    new_tour = [0] + [new_city if x == city_to_replace else x for x in current_cities] + [0]
    return new_tour

def VND(S, distances):
    # Iterate through pairs of indices attempting swaps to find improved tour
    best_tour = S[:]
    best_cost = calculate_total_distance(best_tour, distances)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S)-1):
            for j in range(i+1, len(S)-1):
                if i != j:
                    S[i], S[j] = S[j], S[i]  # Swap cities
                    current_cost = calculate_total_distance(S, distances)
                    if current_cost < best_cost:
                        best_tour = S[:]
                        best_cost = current_cost
                        improved = True
                    S[i], S[j] = S[j], S[i]  # Swap back
    return best_tour

def GVNS(V, k, nrst=10):
    distances = [[euclidean_distance(V[i], V[j]) for j in range(len(V))] for i in range(len(V))]
    best_tour = None
    best_cost = float('inf')

    for _ in range(nrst):
        S = generate_initial_solution(V, k)
        for _ in range(100):  # Number of iterations
            S_prime = shake(S, V, k)
            S_double_prime = VND(S_prime, distances)
            cost_double_prime = calculate_total_distance(S_double_prime, distances)
            if cost_double_prime < best_cost:
                best_tour = S_double_prime
                best_cost = cost_double_prime
                S = S_double_prime

    return best_tour, best_cost

# Define cities coordinates
V = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Find the shortest tour for 4 cities including the depot
tour, total_cost = GVNS(V, 4)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")