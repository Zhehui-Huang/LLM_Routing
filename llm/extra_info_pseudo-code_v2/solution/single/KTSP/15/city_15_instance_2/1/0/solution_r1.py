import random
import math

# Coordinates of cities
cities_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities based on their indices."""
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(tour):
    """Calculate the total distance of the given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """Generate an initial solution by randomly selecting 7 cities in addition to the depot."""
    cities = list(range(1, 15))
    random.shuffle(cities)
    initial = [0] + cities[:7] + [0]
    return initial

def shake(s, k):
    """Perform a shake operation to escape local minima by rearranging a slice."""
    middle = s[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

def local_search(s):
    """Perform local search through swap operations to find a better solution."""
    n = len(s)
    best_s = s[:]
    best_cost = total_distance(s)
    
    for i in range(1, n-1):
        for j in range(i+1, n-1):
            s_new = s[:]
            s_new[i], s_new[j] = s_new[j], s_new[i]
            new_cost = total_distance(s_new)
            if new_cost < best_cost:
                best_s = s_new[:]
                best_cost = new_cost
    
    return best_s

def gvns(k_max, itermax):
    """The General Variable Neighborhood Search algorithm."""
    s = generate_initial_solution()
    best_s = s[:]
    best_cost = total_distance(s)
    
    for _ in range(itermax):
        for k in range(1, k_max+1):
            s_prime = shake(best_s, k)
            s_prime_prime = local_string(s_prime)
            cost_prime_prime = total_distance(s_prime_prime)
            
            if cost_prime_prime < best_cost:
                best_s = s_prime_prime[:]
                best_cost = cost_prime_prime
                break
    
    return best_s, best_cost

# GVNS parameters
k_max = 3
itermax = 100

# Execute GVNS
optimal_tour, optimal_cost = gvns(k_max, itermax)

# Print the optimal tour and cost
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)