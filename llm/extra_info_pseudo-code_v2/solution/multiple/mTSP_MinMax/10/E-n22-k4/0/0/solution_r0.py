import numpy as np
from itertools import permutations

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def initialize_solution(cities, num_robots):
    distances = [euclidean_distance(cities[0], city) for city in cities[1:]]
    nodes = sorted(range(1, len(cities)), key=lambda x: distances[x-1])
    parts = np.array_split(nodes, num_robots)
    tours = [[0] + part.tolist() + [0] for part in parts]
    return tours

def shake(tours, k):
    flat_tours = [city for tour in tours for city in tour[1:-1]]
    np.random.shuffle(flat_tours)
    new_tours = list(np.array_split(flat_tours, len(tours)))
    return [[0] + list(tour) + [0] for tour in new_tours]

def seq_vnd(tours, cities):
    def two_opt(tour):
        best_distance = calculate_tour_distance(tour, cities)
        best_tour = tour[:]
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_tour_distance(new_tour, cities)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_tour = new_tour
        return best_tour

    improved = True
    while improved:
        improved = False
        for i in range(len(tours)):
            new_tour = two_opt(tours[i])
            if new_tour != tours[i]:
                tours[i] = new_tour
                improved = True
    return tours

def gvns(cities, num_robots, kmax, tmax):
    tours = initialize_solution(cities, num_robots)
    start_time = time.time()
    while time.time() - start_time < tmax:
        k = 1
        while k <= kmax:
            new_tours = shake(tours, k)
            new_tours = seq_vnd(new_tours, cities)
            if all(calculate_tour_distance(new_tour, cities) < calculate_tour_distance(tour, cities) for new_tour, tour in zip(new_tours, tours)):
                tours = new_tours[:]
                k = 1
            else:
                k += 1
    return tours

# City data
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_robots = 4
tours = gvns(cities, num_robots, kmax=10, tmax=60)  # kmax and tmax are hyperparameters to adjust

# Calculate costs and find max
costs = [calculate_tour_distance(tour, cities) for tour in tours]
max_cost = max(costs)

for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")