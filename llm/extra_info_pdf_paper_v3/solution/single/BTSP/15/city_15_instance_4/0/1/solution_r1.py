import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp_min_max(cities):
    n = len(cities)
    dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Starting at the depot city, which is city_0
    tour = [0]
    remaining_cities = set(range(1, n))
    
    # Find next city based on the nearest neighbor (Greedy approach)
    while remaining_cities:
        last_city = tour[-1]
        next_city = min(remaining_cities, key=lambda x: dist[last_city][x])
        tour.append(next_city)
        remaining_cities.remove(next_city)

    # Returning to the starting city (depot)
    tour.append(0)

    # Calculate the total cost and the maximum distance between consecutive cities
    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Define cities coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Solve the problem
tour, total_cost, max_distance = solve_tsp_min_max(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")