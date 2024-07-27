import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Determine the distances between each pair of cities
def calculate_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate an initial possible tour (only a heuristic or naive example)
def initial_tour():
    remaining_cities = list(cities.keys())[1:]  # cities excluding the start depot city 0
    chunks = len(remaining_cities) // 8
    return [remaining_cities[i*chunks:(i+1)*chunks] for i in range(8)]

# Create naive tours
tours = initial_tour()
for i in range(len(tours)):
    tours[i].insert(0, 0)
    tours[i].append(0)

# Calculate tour cost
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Calculating costs and optimizing each route
total_overall_cost = 0
finalized_tours = []

for idx, tour in enumerate(tours):
    min_cost = float('inf')
    best_local_tour = None
    
    # Use permutations to explore better routes quickly (this is not efficient for larger numbers of cities)
    for perm in permutations(tour[1:-1]):
        perm = [0] + list(perm) + [0]
        cost = tour_cost(perm)
        if cost < min_cost:
            min_cost = cost
            best_local_tour = perm
    
    finalized_tours.append(best_local_tour)
    total_overall_cost += min_cost
    print(f"Robot {idx} Tour: {best_local_tour}")
    print(f"Robot {idx} Total Travel Cost: {min_cost:.2f}")

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")