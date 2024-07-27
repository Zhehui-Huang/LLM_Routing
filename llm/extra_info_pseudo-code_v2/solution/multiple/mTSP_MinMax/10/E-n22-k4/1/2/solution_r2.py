import math
import random
import time

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def initial_solution():
    cities = list(range(1, len(coordinates)))
    random.shuffle(cities)
    tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(cities):
        tours[i % num_robots].append(city)
    return tours

def calculate_tour_cost(tour):
    if not tour:
        return 0
    cost = euclidean_distance(0, tour[0]) + euclideandistance(tour[-1], 0)
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    return cost

def shake(tours, k):
    for _ in range(k):
        src = random.randint(0, num_robots-1)
        if tours[src]:
            city = tours[src].pop(random.randint(0, len(tours[src])-1))
            dest = random.randint(0, num_robots-1)
            tours[dest].append(city)

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(len(tour) - 1):
            for j in range(i + 2, len(tour)):
                if euclidean_distance(tour[i], tour[j]) + euclidean_distance(tour[i+1], tour[j+1]) < euclidean_distance(tour[i], tour[i+1]) + euclidean_distance(tour[j], tour[j+1]):
                    tour[i+1:j+1] = reversed(tour[i+1:j+1])
                    improved = True

num_robots = 4
def gvns(tmax=10):
    tours = initial_solution()
    start_time = time.time()
    while time.time() - start_time < tmax:
        for k in range(1, 5):
            new_tours = [list(t) for t in tours]
            shake(new_tours, k)
            for tour in new_tours:
                two_opt(tour)
            if max(map(calculate_tour_cost, new_tours)) < max(map(calculate_tour_cost, tours)):
                tours = new_tours
                break
    return tours

tours = gvns()
max_cost = 0
for i, tour in enumerate(tours):
    tour_with_depot = [0] + tour + [0]
    cost = calculate_tour_cost(tour)
    max_cost = max(max_cost, cost)
    print(f"Robot {i} Tour: {tour_with_depot}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Travel Cost: {max_cost}")