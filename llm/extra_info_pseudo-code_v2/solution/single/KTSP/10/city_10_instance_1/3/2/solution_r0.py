import random
import math
from itertools import permutations

# City coordinates indexed by city number
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities given their indices."""
    x1, y1 = coordinates[c1]
    x2, y2 = coordinates[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution(k):
    """Generate a random initial solution with exactly k cities including the depot."""
    cities = list(coordinates.keys())  # All available city indices
    random.shuffle(cities)  # Shuffle to get random order
    
    # Ensure depot city 0 is included
    if 0 not in cities[:k]:
        cities.remove(0)
        cities.insert(0, 0)
    
    return cities[:k] + [0]  # Include depot at the end for a round trip

def shake(solution, k):
    """Perform a shake on the solution by randomly swapping two cities except the depot."""
    s_prime = solution[:-1]  # Do not include the final return to depot city
    a, b = random.sample(range(1, k-1), 2)  # Pick two indices to swap, not touching the depot city
    s_prime[a], s_prime[b] = s_prime[b], s_prime[a]
    return s_prime + [0]

def local_search(solution):
    """Try all pairwise swaps to find the best local move."""
    best_distance = total_tour_distance(solution)
    best_solution = solution[:]
    
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            candidate_solution = solution[:]
            candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
            current_distance = total_tour_distance(candidate_solution)
            if current_distance < best_distance:
                best_distance = current_distance
                best_solution = candidate_solution[:]
                
    return best_solution

def gvns(k, max_iter, max_no_improvement):
    """Implement the GVNS algorithm."""
    best_solution = generate_initial_solution(k)
    best_cost = total_tour_distance(best_solution)
    no_improvement = 0
    
    for _ in range(max_iter):
        if no_improvement >= max_no_improvement:
            break
        shaken_solution = shake(best_solution, k)
        new_solution = local_search(shaken_solution)
        new_cost = total_tour_distance(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_seconds
            no_improvement = 0
        else:
            no_improvement += 1
            
    return best_solution, best_cost

# Settings
k = 5  # Including the depot city
max_iter = 1000
max_no_improvement = 100

# Execute
tour, cost = gvns(k, max_iter, max_no_improvement)

print("Tour:", tour)
print("Total travel cost:", cost)