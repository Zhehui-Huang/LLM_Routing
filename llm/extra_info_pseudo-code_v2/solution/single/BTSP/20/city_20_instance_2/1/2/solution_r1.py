import math

def euclidean_distance(p1, p2):
    """Calculates Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_distance_matrix(cities):
    """Computes distance matrix for the given list of cities."""
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_approximate_tour(cities):
    """Finds an approximate Hamiltonian circuit using the nearest neighbor heuristic."""
    n = len(cities)
    distances = compute_distance_matrix(cities)
    unvisited = set(range(1, n))
    tour = [0]
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next, city)
        current = next_city

    tour.append(0)  # return to the depot
    return tour

def calculate_tour_cost(distances, tour):
    """Calculates the total and maximum consecutive distances of a tour."""
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Coordinates of the cities: (city_0 is the depot)
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Computing the TSP tour using a nearest neighbor heuristic (from the depot)
tour = find_approximate_tour(cities)
distances = compute_distance_matrix(cities)
total_cost, max_distance = calculate_tour_cost(distances, tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")