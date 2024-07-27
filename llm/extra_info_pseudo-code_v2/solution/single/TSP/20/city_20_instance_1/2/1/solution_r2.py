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
    return math.sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

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
        next_city = min(unvisited, key=lambda x: euclidean_distance(last, x))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)  # returning to the depot
    return tour

def lin_kernighan_heuristic(tour):
    """Simple simulated improvement over given tour by reversing segments (2-opt like approach)"""
    best_tour = tour[:]
    best_distance = calculate_total_distance(tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(best_tour) - 1):
            for j in range(i + 2, len(best_tour)):
                if j - i == 1: continue  # skip adjacent edges
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True

    return best_tour, best_distance

# Main execution setup
cities = list(range(20))
initial_tour = nearest_neighbor_tour(0, cities)
optimized_tour, total_cost = lin_kernighan_heuristic(initial_tour)

# Correct output
print("Tour:", optimized_tour)
print("Total travel cost:", round(total_cost, 2))