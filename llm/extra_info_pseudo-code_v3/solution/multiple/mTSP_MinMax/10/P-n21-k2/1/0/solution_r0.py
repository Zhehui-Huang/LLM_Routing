import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Define the number of robots
num_robots = 2

# Function to calculate the euclidean distance between cities
def distance(city1, city2):
    return np.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Function to cluster cities (excluding the depot)
def cluster_cities():
    city_coords = [coords for key, coords in cities.items() if key != 0]
    kmeans = KMeans(n_clusters=num_robots).fit(city_coords)
    clusters = {i: [] for i in range(num_robots)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # +1 because we removed the depot from city list
    return clusters

# 2-opt heuristic to improve the tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # no change for consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if cost_tour(new_tour) < cost_tour(tour):
                    tour = new_tour
                    improved = True
    return tour

def cost_tour(tour):
    total_cost = 0
    for k in range(len(tour) - 1):
        total_cost += distance(tour[k], tour[k + 1])
    return total_cost

def solve_tsp():
    clusters = cluster_cities()
    tours = []
    
    for k in sorted(clusters.keys()):
        tour = [0] + clusters[k] + [0]
        optimized_tour = two_opt(tour)
        tours.append(optimized_tour)
    
    max_cost = 0
    for index, tour in enumerate(tours):
        tour_cost = cost_tour(tour)
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {tour_cost}")
        if tour_cost > max_cost:
            max_cost = tour_cost
            
    print(f"Maximum Travel Cost: {max_cost}")

# Run the solution
solve_tsp()