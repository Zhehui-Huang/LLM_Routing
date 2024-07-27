import numpy as np

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots
num_robots = 2
depot = 0

# Create clusters for initial distribution assuming equal division of cities
city_ids = list(cities.keys())[1:]  # Exclude depot
np.random.shuffle(city_ids)
clusters = [city_ids[i::num_robots] for i in range(num_robots)]

# Initialize tours
tours = [[depot] + cluster + [depot] for cluster in clusters]

def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Apply 2-opt algorithm for tour improvement
def apply_two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Adjacent edges
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improved = True
        if improved:
            break
    return tour

# Optimize each tour using 2-opt
optimized_tours = [apply_two_opt(tour) for tour in tours]

# Output results
overall_total_cost = 0
for idx, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    overall_total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Difference Cost: {overall_total_cost:.2f}")