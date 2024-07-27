import math

def calculate_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue # consecutive edges
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(distance_matrix[best[k]][best[k + 1]] for k in range(len(best) - 1)) > sum(distance_matrix[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

def nearest_neighbor_tour(initial_city, cities, distance_matrix):
    tour = [initial_city]
    unvisited = set(cities)
    unvisited.remove(initial_city)
    
    current = initial_city
    while unvisited:
        next_city = min(unverified, key=lambda city: distance_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(initial_city)  # return to depot
    return tour

# Set up the problem
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
num_robots = 4
depot = 0
cities = list(range(1, len(coords)))

# Distance matrix computation
distance_matrix = [[calculate_distance(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]

# Initial naive tour distribution and nearest neighbor tour construction
clusters = {i: [] for i in range(num_robots)}
for i, city in enumerate(sorted(cities, key=lambda x: distance_matrix[depot][x])):
    clusters[i % num_robots].append(city)

tours = [nearest_neighbor_tour(depot, cluster, distance_matrix) for cluster in clusters.values()]

# Improve each tour using 2-opt
optimized_tours = [two_opt(tour, distance_matrix) for tour in tours]

# Calculate and display results
total_cost = 0

for idx, tour in enumerate(optimized_tours):
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}\n")

print("Overall Total Travel Cost:", total_cost)