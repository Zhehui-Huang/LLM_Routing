import math
import random

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
    cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return cost

def generate_initial_solution(home_city, k):
    """Generate a random initial solution with k cities excluding the home city."""
    city_list = list(cities.keys())
    city_list.remove(home_city)
    selected_cities = random.sample(city_list, k-1)
    tour = [home_city] + selected_cities + [home_city]
    return tour

def perform_local_search(tour):
    """Peforms local search optimization by exploring all 2-opt moves (swapping two cities)."""
    min_tour_cost = tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i+1, len(best_tour) - 1):
                if i != 0 and j != len(best_tour) - 1:  # Do not swap the home city
                    new_tour = best_tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = tour_cost(new_tour)
                    if new_cost < min_tour_cost:
                        best_tour = new_tour[:]
                        min_tour_cost = new_cost
                        improved = True
    return best_tour

def gvns(k, num_restarts=1000):
    best_tour = None
    best_cost = float('inf')
    for _ in range(num_restarts):
        initial_tour = generate_initial_solution(0, k)
        optimized_tour = perform_local_search(initial_tour)
        cost = tour_cost(optimized_tour)
        if cost < best_cost:
            best_tour = optimized_tour
            best_cost = cost
    return best_tour, best_cost

# Running the algorithm for k = 4 cities including the home city.
k = 4
best_tour, best_cost = gvns(k)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)