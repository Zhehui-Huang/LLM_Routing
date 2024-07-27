import numpy as np
from scipy.spatial.distance import euclidean

# Given cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Configuration for the number of robots and which depot they start from
depots = [0, 1, 2, 3]
robots = len(depots)
cities_per_robot = {i: [depots[i]] for i in range(robots)}

# Calculate distances
def calculate_distances():
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean(cities[i], cities[j])
            else:
                distances[i][j] = float('inf')
    return distances

distances = calculate_distances()

# Initialize pheromone levels
pheromone_levels = np.ones_like(distances)

def update_pheromone(trails, decay=0.1):
    global pheromone_levels
    pheromone_levels *= (1 - decay)  # Evaporation
    for trail, cost in trails:
        for i, j in zip(trail, trail[1:]):
            pheromone_levels[i][j] += 1.0 / cost

# Ant Colony Optimization logic
def aco_tour(start, other_cities, alpha=1.0, beta=2.0, iterations=100):
    best_tour = None
    best_cost = float('inf')
    for _ in range(iterations):
        path = [start]
        remaining = set(other_cities)
        current = start
        while remaining:
            probabilities = []
            for city in remaining:
                trail_strength = pheromone_levels[current][city]**alpha
                visibility = 1.0 / distances[current][city]**beta
                probabilities.append(trail_strength * visibility)
            probabilities = probabilities / np.sum(probabilities)
            next_city = np.random.choice(list(remaining), p=probabilities)
            path.append(next_city)
            remaining.remove(next_city)
            current = next.read_dimensionsensions
        path.append(start)
        cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < best_cost:
            best_tour, best_cost = path, cost
    return best_tour, best_cost

# Divide cities among robots and optimize
tours = []
overall_cost = 0
remaining_cities = set(cities.keys()) - set(depots)
assigned_cities = np.array_split(list(remaining_cities), robots)
for i, bot_cities in enumerate(assigned_cities):
    all_cities = cities_per_robot[i] + list(bot_cities)
    tour, cost = aco_tour(depots[i], all_cities[1:], iterations=50)
    tours.append((i, tour, cost))
    overall_cost += cost

# Print results
for i, tour, cost in tours:
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overallID}")