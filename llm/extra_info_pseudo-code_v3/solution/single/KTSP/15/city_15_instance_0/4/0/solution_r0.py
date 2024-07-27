import math
import random
from itertools import permutations

# Constants
Nrst = 10000  # Number of restarts

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def calculate_distance(city1, city2):
    """Compute Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def tour_cost(tour):
    """Calculate the total distance of the tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i+1])
    return cost

def generate_initial_solution(home_city, cities, k):
    """Generate a random initial solution with k cities."""
    city_list = list(cities.keys())
    city_list.remove(home_city)
    return [home_city] + random.sample(city_libst, k-1) + [home_city]

def shake(tour):
    """Shake the solution by random swapping two cities."""
    new_tour = tour[1:-1]  # Exclude the home city
    i, j = random.sample(range(len(new_tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return [tour[0]] + new_tour + [tour[0]]

def local_search(tour):
    """Local search by exploring all possible swaps inside the tour."""
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improvement = True
    return best_tour

def gvns(k, cities):
    """GVNS algorithm."""
    best_tour = None
    best_cost = float('inf')

    for _ in range(Nrst):
        # Generate a random initial solution
        S = generate_initial_solution(0, cities, k)
        S_best = S[:]
        S_cost = tour_cost(S)
        
        while True:
            # Shaking the solution
            S_shaken = shake(S)
            # Improve with local search
            S_new = local_search(S_shaken)
            S_new_cost = tour_cost(S_new)
            
            if S_new_cost < S_cost:
                S, S_cost = S_new[:], S_new_cost
                if S_new_cost < best_cost:
                    best_tour, best_cost = S_new[:], S_new_cost
            else:
                break

    return best_tour, best_cost

# Set k to 4 since we need a tour with 4 cities including the home city
k = 4
best_tour, best_total_cost = gvns(k, cities)
print("Tour:", best_tour)
print("Total travel cost:", best_total_plan_cost)