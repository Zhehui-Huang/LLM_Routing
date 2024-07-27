import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Cartesian distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate total cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Greedy k-TSP heuristic
def k_tsp_greedy(depot, k):
    unvisited = set(cities.keys())
    unvisited.remove(depot)
    tour = [depot]
    
    while len(tour) < k:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(last_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    
    tour.append(depot) # Return to depot
    return tour

# Find the shortest tour using all permutations of 6 cities chosen from 1 to 9
def k_tsp_optimal(depot, k):
    best_tour = None
    best_cost = float('inf')
    cities_to_choose = list(cities.keys())
    cities_to_choose.remove(depot)
    
    for selected_cities in permutations(cities_to_choose, k - 1):  # k - 1 because we always include the depot
        tour = [depot] + list(selected_cities) + [depot]
        cost = tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
            
    return best_tour, best_cost

# Perform the search
best_tour, best_cost = k_tsp_optimal(0, 7)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))