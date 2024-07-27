import math

# Cities coordinates
coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)

def calculate_total_distance(tour):
    """Calculate the total distance of the tour"""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(start, cities):
    """Generate a simple tour using the nearest neighbor heuristic"""
    tour = [start]
    unvisited = set(cities)
    unvisited.remove(start)

    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: euclidean_address(last, x))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)  # return to the depot
    return tour

def lin_kernighan_heuristic(tour):
    """Placeholder for Lin-Kernighan algorithm; using 2-opt-like steps instead."""
    # Here we'll use a simple simulated version of the LK heuristic,
    # continuing from the pseudocode using neighborhood change strategies
    best_tour = tour[:]
    best_distance = calculate_total_distance(tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # skip adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_cond_distance
                    improved = True
        tour = best_tour

    return best_tour, best_distance

# Setup for starting the solution
cities = list(range(20))
initial_tour = nearest_neighbor_tour(0, cities)
optimized_tour, total_cost = lin_kernighan_heuristic(initial_tour)

# Output the results correctly
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)