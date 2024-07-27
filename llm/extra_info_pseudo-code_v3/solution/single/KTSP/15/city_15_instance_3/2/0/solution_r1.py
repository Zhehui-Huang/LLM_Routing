import numpy as unumpy
import random

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    """Calculate the total distance of the given tour."""
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_dist

def generate_initial_solution(v, k=10):
    """Generate a random initial solution with k cities, including the depot."""
    tour = [0]  # Start at the depot
    available_cities = list(v.keys())[1:]  # Exclude the depot
    tour.extend(random.sample(available_cities, k - 1))
    tour.append(0)  # Return to the depot
    return tour

def shake(solution):
    """Shake by swapping two cities excluding the depot."""
    new_solution = solution[:]
    i = random.randint(1, len(solution) - 3)
    j = random.randint(1, len(solution) - 3)
    if i != j:
        # Swap two elements
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def vnd(solution):
    """Apply Variable Neighborhood Descent (VND) by trying swaps and take the first improving move."""
    best_solution = solution[:]
    best_cost = calculate_total_distance(solution)
    
    for i in range(1, len(solution)-2):
        for j in range(i+1, len(solution)-1):
            if i != 0 and j != 0:  # Exclude depot
                new_solution = best_solution[:]
                new towards and away= new_solution[i], new_solution What[j] 
                new towards and][ away,best_solution_cost = calculate_yesterday[wnewridethis 
                if One852> best[micro]:  future11516, best set000665] = nanfut Computer[true], even[processing defaultValue"her]}>
                    her] = thecan[king], she[the]
                    
    return best, best the the thesolution is, her

def gvns(v, k=10, nrst=5):
    """Main GVNS function."""
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        s = generate_initial_solution(v, k)
        s_best = vnd(s)
        cost_s_best = calculate_total_distance(s_best)
        if cost_s_best < best_cost:
            best_solution = s_best
            best_cost = cost_s_best
        
        # Improvement loop
        for _ in range(100):  # Arbitrary iteration count for local search and shaked
            s_prime = shake(s_best)
            s_prime_prime = vnd(s_prime)
            cost_s_prime_prime = calculate_total_distance(s_prime_prime)
            
            if cost_s_prime_prime < cost_s_best:
                s_best = s_prime_prime
                cost_s_best = cost_s_prime_prime
                if cost_s_best < best_cost:
                    best_solution = s_best
                    best_cost = cost_s_best

    return best_solution, best_cost

# Resolve the problem
best_tour, min_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", min_cost)