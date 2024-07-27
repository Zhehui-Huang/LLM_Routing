import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_tours(depot, cities):
    # Distance from depot sorted access
    distances = [(i, euclidean_distance(depot, city)) for i, city in enumerate(cities)]
    distances.sort(key=lambda x: x[1])
    
    # Initialization of tours
    tours = {0: [0, distances[0][0], 0], 1: [0, distances[1][0], 0]}
    for i in range(2, len(distances)):
        best_tour = min(tours.keys(), key=lambda x: euclidean_distance(cities[tours[x][-2]], cities[distances[i][0]]))
        tours[best_tour].insert(-1, distances[i][0])
    
    return tours

def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def shake(tours, cities, k=3):
    keys = list(tours.keys())
    while k > 0:
        v = random.choice(keys)
        t = random.choice([tk for tk in keys if tk != v])
        if len(tours[v]) > 3:
            node = random.choice(tours[v][1:-1])
            tours[v].remove(node)
            tours[t].insert(-1, node)
            k -= 1
    return tours

def local_search_best_improvement(tour, cities):
    best_cost = calculate_tour_cost(tour, cities)
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            # 2-opt swap
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            new_cost = calculate_tour_cost(new_tour, cities)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
    return best_tour

def main_gvns(cities, robots=2, lmax=5, kmax=5, tmax=30):
    depot = cities[0]
    non_depot_cities = cities[1:]
    
    # Initial solution
    tours = initialize_tours(depot, non_depot_cities)
    
    # Start the main GVNS loop
    best_tours = tours
    best_max_cost = max(calculate_tour_cost(tours[k], [depot] + non_depot_cities) for k in tours)
    
    for iteration in range(tmax):
        # Shaking Phase
        tours = shake(tours, [depot] + non_depot_cities)
        
        # Local search phase
        for k in tours:
            new_tour = local_search_best_improvement(tours[k], [depot] + non_depot_cities)
            tours[k] = new_tour
        
        # Check improvement
        current_max_cost = max(calculate_tour_cost(tours[k], [depot] + non_depot_cities) for k in tours)
        if current_max_cost < best_max_cost:
            best_max_cost = current_max_cost
            best_tours = {k: tours[k][:] for k in tours}

    # Output the results
    for robot_id, tour in best_tours.items():
        cost = calculate_tour_cost(tour, [depot] + non_depot_cities)
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")

    print(f"Maximum Travel Cost: {best_max_cost}")

# Provided coordinates of cities
cities = [
    (30, 40), # depot city
    (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
main_gvns(cities, robots=2)