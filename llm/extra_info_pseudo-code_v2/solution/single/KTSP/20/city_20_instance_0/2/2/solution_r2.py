import math
import random

# Coordinates of the cities (indexed from 0 to 19)
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Constants for the problem
k = 4  # Total cities to visit including the depot
itermax = 1000
pmax = 2

def distance(city1, city2):
    """Calculate Euclidean distance between two city indices."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def evaluate_tour(tour):
    """Calculate the total distance of the given tour."""
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """Generate a random initial tour including the depot."""
    cities = list(range(1, len(coordinates)))
    selected_cities = random.sample(cities, k-1)
    tour = [0] + selected_cities + [0]
    return tour

def shake(tour, p):
    """Shake the tour by altering its structure slightly."""
    internal_cities = tour[1:-1]
    if p == 1:  # Swap two cities
        i, j = random.sample(range(len(internal_cities)), 2)
        internal_cities[i], internal_cities[j] = internal_cities[j], internal_cities[i]
    elif p == 2:  # Reverse a sub-section
        if len(internal_cities) > 1:
            start, end = sorted(random.sample(range(len(internal_cities)), 2))
            internal_cities[start:end+1] = reversed(internal_cities[start:end+1])
    return [0] + internal_cities + [0]

def local_search(tour):
    """Improve the tour using local modifications."""
    best_tour = tour[:]
    best_cost = evaluate_tour(tour)
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = evaluate_tour(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    made_improvement = True
    return best_tour

def gvns():
    """General Variable Neighborhood Search algorithm to solve the problem."""
    best_solution = generate_initial_solution()
    best_cost = evaluate_tour(best_solution)
    
    for _ in range(itermax):
        current_solution = best_solution[:]
        for p in range(1, pmax+1):
            shaken_solution = shake(current_solution, p)
            improved_solution = local_search(shaken_solution)
            cost = evaluate_tour(improved_solution)
            if cost < best_cost:
                best_solution, best_cost = improved_solution[:], cost
                break  # Break to restart with p = 1
    return best_solution, best_cost

# Run the GVNS algorithm
best_tour, total_cost = gvns()

# Printing the tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")