import numpy as np

# City Coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Total cost of a given tour
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance(tour[i-1], tour[i])
    cost += distance(tour[-1], tour[0])  # Complete the cycle
    return cost
    
def improved_tour(initial_tour):
    k = len(initial_tour)
    tour = initial_tour.copy()
    best_cost = tour_cost(tour)
    
    # Local Optimization by 2-opt heuristic
    improved = True
    while improved:
        improved = False
        for i in range(1, k - 1):
            for j in range(i + 1, k):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour, best_cost, improved = new_tour, new_cost, True
                    
    return tour, best_cost

def find_best_tour():
    k = 6  # Total, including the depot
    best_tour = []
    best_cost = float('inf')

    for subset in itertools.combinations(list(cities.keys())[1:], k-1):
        current_tour = [0] + list(subset) + [0]
        optimized_tour, optimized_cost = improved_tour(current_tour)
        
        if optimized_cost < best_cost:
            best_tour, best_cost = optimized_tour, optimized_cost
                        
    return best_tour, best_cost

# Perform the search for the best tour
best_tour, best_cost = find_best_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")