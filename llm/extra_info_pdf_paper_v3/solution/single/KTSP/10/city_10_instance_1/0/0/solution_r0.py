import itertools
import math

# City coordinates
cities = {
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
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def k_tsp(cities_to_visit):
    shortest_tour = None
    min_cost = float('inf')
    
    # Generate all permutations of the selected cities + depot
    for perm in itertools.permutations(cities_to_visit):
        # Adding depot to the start and end of the list
        current_tour = [0] + list(perm) + [0]
        current_cost = total_tour_cost(current_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour
    
    return shortest_tour, min_cost

def solve_k_tsp_k_equals_5():
    all_non_depot_cities = list(cities.keys())[1:]  # Exclude the depot
    best_tour = None
    best_cost = float('inf')

    # Generate all combinations of 4 cities from non-depot cities
    for combo in itertools.combinations(all_non_depot_cities, 4):
        cities_to_visit = list(combo)
        tour, cost = k_tsp(cities_to_visit)
        
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    
    return best_tour, best_cost

# Compute the solution
tour, total_cost = solve_k_tsp_k_equals_5()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")