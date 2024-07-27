import math
import itertools

# City coordinates
cities = [
    (3, 26),   # Depot city
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48),  # City 19
]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute distances between each pair of cities
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Implement the nearest neighbor heuristic to select 10 cities starting from the depot
def find_tour(start_city, num_cities):
    unvisited = set(range(n))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_stuff

    while len(tour) < num_cities:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    # Close the tour by returning to the start city
    tour.append(start_city)
    return tour

# Get the initial greedy tour with 10 cities
initial_tour = find_tour(0, 10)

# Calculate the cost of a tour
def calculate_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Find the best permutation of the 10 cities to minimize the tour length
best_tour = None
best_cost = float('inf')
for perm in itertools.permutations(initial_tour[1:-1]):
    candidate_tour = [initial_tour[0]] + list(perm) + [initial_tour[0]]
    cost = calculate_cost(candidate_tour)
    if cost < best_cost:
        best_tour = candidate_tour
        best_cost = cost

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")