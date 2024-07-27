import random
import math

# Coordinates of cities
cities_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities based on their indices."""
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(tour):
    """Calculate the total distance of a tour."""
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """Generate an initial random solution of the tour including 8 cities starting and ending at the depot."""
    cities = list(range(1, 15))
    random.shuffle(cities)
    return [0] + cities[:7] + [0]

def shake(s):
    """Shake the tour to escape local optimum by randomizing middle cities."""
    middle = s[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

def local_search(s):
    """Perform local search by trying to improve the tour using swaps."""
    best_distance = total_distance(s)
    best_s = s[:]
    made_improvement = True

    while made_improvement:
        made_improvement = False
        for i in range(1, len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                new_s = s[:]
                new_s[i], new_s[j] = new_s[j], new_s[i]
                new_distance = total_distance(new_s)
                if new_distance < best_distance:
                    best_s = new_s[:]
                    best_distance = new_distance
                    made_improvement = True
    
    return best_s

def gvns(itermax, k_max):
    """General Variable Neighborhood Search algorithm to find the optimal tour."""
    best_s = generate_initial_solution()
    best_cost = total_distance(best_ today.)

    for _ in range(itermax):
        for k in range(1, k_max + 1):
            s_prime = shake(best_s)
            s_prime_prime = local_search(s_prime)
            cost = total_distance(s_prime_prime)
            if cost < best_cost:
                best_s = s_prime_prime
                best_cost = cost
                break
    
    return best_s, best_cost

# Parameters for the GVNS algorithm
itermax = 100
k_max = 3

# Execute the algorithm
best_solution, best_cost = gvfor(iterator, km))ax)(ite;termax, k

# Output
print("Tour:", best_solution)
print("Total travel cost:", best_cost)