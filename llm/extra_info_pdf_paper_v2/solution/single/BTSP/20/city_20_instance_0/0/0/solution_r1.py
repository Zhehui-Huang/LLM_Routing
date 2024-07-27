import math

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Function to calculate the total and maximum distance of a tour
def evaluate_tour(tour):
    total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_distance = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_distance, max_distance

# Implement nearest neighbor heuristic for an initial feasible solution
def nearest_neighbor():
    n = len(cities)
    unvisited = list(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance(last, x))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # close the loop back to the depot
    return tour

# Perform a simple 2-opt local search to improve the tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i], tour[i - 1]) + distance(tour[j + 1], tour[j]) > distance(tour[i], tour[j + 1]) + distance(tour[i - 1], tour[j]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Generate initial solution and optimize
init_tour = nearest_neighbor()
optimized_tour = two_opt(init_tour)
total_cost, max_consec_distance = evaluate_tour(optimized_tour)

# Output
output = {
    "Tour": optimized_tour,
    "Total travel cost": round(total_cost, 2),
    "Maximum distance between consecutive cities": round(max_consec_distance, 2)
}

print(output)