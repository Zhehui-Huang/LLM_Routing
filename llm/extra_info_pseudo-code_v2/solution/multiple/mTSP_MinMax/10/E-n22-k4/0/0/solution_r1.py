import numpy as np
import time

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_distance(tour, cities):
    distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return distance + euclidean_distance(cities[tour[-1]], cities[tour[0]])

def initialize_solution(cities, num_robots):
    distances = [euclidean_distance(cities[0], city) for city in cities[1:]]
    nodes = sorted(range(1, len(cities)), key=lambda x: distances[x-1])
    parts = np.array_split(nodes, num_robots)
    tours = [[0] + part.tolist() + [0] for part in parts]
    return tours

def shake(tours, k):
    for _ in range(k):
        # Picking a random tour to remove a city
        tour_idx = np.random.randint(len(tours))
        if len(tours[tour_idx]) > 3:  # Need at least three points to remove one (start, city, end)
            city_idx = np.random.randint(1, len(tours[tour_idx])-1)
            city = tours[tour_idx].pop(city_idx)
            
            # Randomly selecting another tour to receive the city
            receiving_tour_idx = np.random.randint(len(tours))
            receiving_city_idx = np.random.randint(1, len(tours[receiving_tour_idx]))
            tours[receiving_tour_idx].insert(receiving_city_idx, city)
    return tours

def seq_vnd(tours, cities):
    improved = True
    while improved:
        improved = False
        for i in range(len(tours)):
            original_tour = tours[i][:]
            new_tour = two_opt(tours[i], cities)
            if new_tour and calculate_tour_distance(new_tour, cities) < calculate_tour_distance(original_tour, cities):
                tours[i] = new_tour
                improved = True
    return tours

def two_opt(tour, cities):
    best_tour = tour[:]
    best_distance = calculate_tour_distance(tour, cities)
    for i in range(1, len(tour) - 1):
        for j in range(i + 1, len(tour) - 1):
            if j - i == 1: continue  # Skip adjacent cities because they produce the same tour
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            new_distance = calculate_tour_distance(new_tour, cities)
            if new_distance < best_distance:
                best_tour = new_tour
                best_distance = new_distance
    return best_tour if best_tour != tour else None

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
                k = 1  # Reset shaking index if improvement found
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
kmax = 10
tmax = 60  # Adjust time limits accordingly for practical testing or real-world usage

tours = gvns(cities, num_robots, kmax, tmax)

# Calculate costs and find max
costs = [calculate_tour_distance(tour, cities) for tour in tours]
max_cost = max(costs)

for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")