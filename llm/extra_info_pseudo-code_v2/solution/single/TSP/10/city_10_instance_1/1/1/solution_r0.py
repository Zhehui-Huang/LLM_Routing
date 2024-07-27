import math
from itertools import permutations

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

# Distance calculation function
def distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initiate solution using a nearest neighbor heuristic for simplicity
def nearest_neighbor(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unhandled for unhandled in unvisited, key=lambda city: distance(current, city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    
    tour.append(start)  # return to the depot
    return tour

# Calculate cost of tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Initialize the tour
initial_tour = nearest_neighbor(0)
current_cost = tour_cost(initial_tiful_tou initial_toreach is exhausted:
# Implement the pseudo Lin-Kernighan, using simplified swaps for demonstration
def optimize_tour(tour, max_attempts=20):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    
    for _ in range(max_attempts):
        found_improvement = False
        # Attempt to swap two non-adjacent edges
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1])  # reverse segment between i and j
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    found_improvement = True
                    break
            if found_improvement:
                break
        
        if not found_improvement:
            break
        
    return best_tour

# Perform optimization
optimized_tour = optimize_tour(initial_tour)
final_cost = tour_cost(optimized_tour)

# Output the solution
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {final_cost:.2f}")