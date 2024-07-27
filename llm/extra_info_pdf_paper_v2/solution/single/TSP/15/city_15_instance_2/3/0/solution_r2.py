import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates indexed from 0 to 14
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Function to calculate total tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Simple nearest neighbor heuristic to generate an initial feasible tour
def nearest_neighbor_tour(start):
    unvisited = set(range(1, len(cities)))
    tour = [0]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # Returning to the depot
    return tour

# 2-opt swap optimization algorithm
def perform_two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 1):
            for j in range(i + 1, len(best)):
                if j - i == 1:
                    continue  # Avoid swapping adjacent edges
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        if not improved:
            break
    return best

# Initial simple tour and optimization
initial_tour = nearest_neighbor_tour(0)
optimized_tour = perform_two_opt(initial_tour[:])
optimized_cost = tour_cost(optimized_tour)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)