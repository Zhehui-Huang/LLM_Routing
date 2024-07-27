import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution(k):
    """Generate an initial random tour starting and ending at the depot (city 0) with k cities."""
    other_cities = list(cities.keys())
    other_cities.remove(0)
    selected_cities = random.sample(other_cities, k-2)
    return [0] + selected_cities + [0]

def local_search(tour):
    """Try to find a better tour by swapping any two cities and checking if it improves the distance."""
    best_distance = total_distance(tour)
    for i in range(1, len(tour)-2):
        for j in range(i+1, len(tour)-1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_distance = total_distance(new_tour)
            if new_distance < best_distance:
                tour = new_tour
                best_distance = new_distance
    return tour

def gvns(k, itermax):
    """Implement the General Variable Neighborhood Search algorithm."""
    best_solution = generate_initial_solution(k)
    best_cost = total_distance(best_solution)
    iter = 0
    while iter < itermax:
        new_solution = generate_initial_solution(k)
        new_solution = local_search(new_solution)
        new_cost = total_distance(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_auth_cost
        iter += 1
    return best_solution, best_cost

# Set the parameters and solve
k = 6  # Number of cities to visit including depot, visit 5 additional cities
itermax = 1000  # Maximum iterations

best_tour, best_tour_cost = gvns(k, itermax)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost}")