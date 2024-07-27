import math
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate the total travel cost and max distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Generate an initial tour starting from the depot (0) using nearest neighbor heuristic
def get_initial_tour():
    unvisited = list(cities.keys())[1:]
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)  # return to the depot
    return tour

# Optimizing the tour using a basic permutation check to minimize maximum leg distance
def optimize_tour(tour):
    best_tour = tour
    best_cost, best_max_distance = evaluate_tour(tour)
    # Evaluate permutations of the mid-section of the route (excluding the depot at start and end)
    for perm in permutations(tour[1:-1]):
        candidate_tour = [0] + list(perm) + [0]
        cost, max_distance = evaluate_tour(candidate_tour)
        if max_distance < best_max_distance:
            best_tour = candidate_tour
            best_cost = cost
            best_max_distance = max_distance
    return best_tour

# Main execution
initial_tour = get_initial_tour()
optimized_tour = optimize_tour(initial_tour)
total_cost, max_distance = evaluate_tour(optimized_tour)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)