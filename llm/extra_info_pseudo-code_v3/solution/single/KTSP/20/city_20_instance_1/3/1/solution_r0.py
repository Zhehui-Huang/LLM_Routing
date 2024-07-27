import math
import random

# The list of coordinates for each city
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(a, b):
    return math.hypot(cities[a][0] - cities[b][0], cities[a][1] - cities[b][1])

def generate_initial_solution(cities, k):
    cities_list = list(cities.keys())
    random.shuffle(cities_list)
    tour = [0] + cities_list[1:k] + [0]  # Start and end at the depot city
    return tour

def calculate_total_distance(tour):
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_distance

def shake(tour):
    """Performs a simple shake by swapping two random cities in the tour."""
    new_tour = tour[1:-1]  # Exclude the depot city 0 which is at start and end
    a, b = random.sample(range(len(new_tour)), 2)
    new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
    return [0] + new_tour + [0]

def vnd(tour):
    """Applies a very simple Variable Neighborhood Descent by trying all pairs of swaps."""
    best_tour = tour[:]
    best_score = calculate_total_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_score = calculate_total_distance(new_tour)
                if new_score < best_score:
                    best_tour, best_score = new_tour[:], new_score
                    improved = True
    return best_tour

def gvns(cities, k, nrst):
    best_tour = generate_initial_solution(cities, k)
    best_score = calculate_total_distance(best_tour)
    
    for _ in range(nrst):
        initial_tour = generate_initial_solution(cities, k)
        current_tour = initial_tour[:]
        
        for _ in range(100):  # Fixed number of iterations for shaking and VND
            shaken_tour = shake(current_tour)
            improved_tour = vnd(shaken_tour)
            improved_score = calculate_total_distance(improved_tour)
            
            if improved_score < best_score:
                best_tour, best_score = improved_tour, improved_score
                current_tour = improved_tour
            else:
                current_tour = shaken_tour  # continue from new base solution

    return best_tour, best_score

# Number of cities in the tour including the depot (6 + 1 because the depot is included twice)
k = 7 + 1
# Number of random restarts
nrst = 10

best_tour, best_score = gvns(cities, k, nrst)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_score:.2f}")