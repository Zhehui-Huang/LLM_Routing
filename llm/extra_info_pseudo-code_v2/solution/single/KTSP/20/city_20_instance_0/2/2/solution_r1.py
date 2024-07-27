import math
import random

# Coordinates of the cities (indexed from 0 to 19)
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Constants for the algorithm
k = 4  # Number of cities in the tour including the depot
itermax = 100
pmax = 2

def distance(city1, city2):
    """Calculate Euclidean distance between two city indices."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def evaluate_tour(tour):
    """Calculate the total travel cost for the given tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_distance

def generate_initial_solution():
    """Generate an initial solution with random cities excluding the depot."""
    cities = list(range(1, len(coordinates)))
    random.shuffle(cities)
    tour = [0] + random.sample(cities, k - 1) + [0]
    return tour

def shake(tour, p):
    """Shake the current solution by swapping or reversing."""
    internal_tour = tour[1:-1]
    if p == 1:  # Perform a simple swap
        i, j = random.sample(range(k - 1), 2)
        internal_tour[i], internal_tour[j] = internal_tour[j], internal_tour[i]
    elif p == 2:  # Reverse a subpart of the tour
        if len(internal_tour) > 2:
            start, end = sorted(random.sample(range(len(internal_tour)), 2))
            internal_tour[start:end+1] = reversed(internal_tour[start:end+1])
    return [0] + internal_tour + [0]

def local_search(tour):
    """Perform local search optimizations."""
    best_tour = tour
    best_cost = evaluate_tour(tour)
    for i in range(1, k-1):
        for j in range(i+1, k):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = evaluate_tour(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
    return best_tour

def gvns():
    """Main procedure for the General Variable Neighborhood Search algorithm."""
    best_solution = generate_initial_solution()
    best_cost = evaluate_tour(best_solution)
    
    for _ in range(itermax):
        p = 1
        while p <= pmax:
            shaken_solution = shake(best_solution, p)
            new_solution = local_search(shaken_solution)
            new_cost = evaluate_tour(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_alert
                break  # Restart the loop with p = 1 since improvement was found
            else:
                p += 1
    
    return best_solution, best_cost

# Find the best tour and the total cost
best_tour, total_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")