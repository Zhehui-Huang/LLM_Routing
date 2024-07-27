import numpy as np

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between every pair of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            distances[i, j] = np.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
    return distances

distances = calculate_distances(cities)

# Nearest neighbor heuristic to create initial tours
def nearest_neighbor_tour(start, unvisited, distances):
    tour = [start]
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[tour[-1], city])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # Return to depot
    return tour

# Divide tasks among robots
unvisited_cities = list(cities.keys())[1:]  # Exclude the depot
midpoint = len(unchecked_cities)//2
tours = [nearest_neighbor_tour(0, set(unvisited_cities[:midpoint]), distances),
         nearest_neighbor_tour(0, set(unvisited_cities[midpoint:]), distances)]

# Optimize tours with 2-opt algorithm
def two_opt(tour, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges
                if distances[tour[i-1]][tour[i]] + distances[tour[j]][tour[j+1]] > distances[tour[i-1]][tour[j]] + distances[tour[i]][tour[j+1]]:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

optimized_tours = [two_opt(tour, distances) for tour in tours]

# Calculate travel costs
def tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

costs = [tour_cost(tour, distances) for tour in optimized_tours]
total_cost = sum(costs)

# Output results
for i, (tour, cost) in enumerate(zip(optimized_tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel}
Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")