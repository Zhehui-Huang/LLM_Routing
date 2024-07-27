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

# Generate an initial tour with a nearest neighbor heuristic starting from the depot
def get_initial_tour():
    unvisited = list(cities.keys())[1:]  # All cities excluding the depot
    tour = [0]  # Start from the depot
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        tour.append(nextthm_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)  # Return to the depot
    return tour

# Find the best tour that minimizes the maximum distance between consecutive cities
def find_best_tour():
    initial_tour = get_initial_tour()
    min_max_distance = float('inf')
    best_tour = None

    for perm in permutations(cities.keys() - {0}):
        tour = [0] + list(perm) + [0]
        _, max_dist = evaluate_tour(tour)
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour

    return best_tour

# Execute the function to get the best tour
best_tour = find_best_tour()
total_cost, max_distance = evaluate_tour(best_tour)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)