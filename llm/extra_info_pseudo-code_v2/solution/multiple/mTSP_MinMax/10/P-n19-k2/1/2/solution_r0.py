import math
import random

# --- Step 1: Basic Settings and Utility Functions ---
# Defining city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance
def distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# --- Step 2: Distance Matrix ---
n = len(cities)
dist_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# --- Step 3: Initialize Routes for Each Robot ---
def initial_solution(num_robots):
    # Sorting cities by distance to the depot (excluding city 0 itself)
    sorted_cities = sorted(list(cities.keys())[1:], key=lambda x: distance(0, x))
    tours = [[] for _ in range(num_robots)]
    for index, city in enumerate(sorted_cities):
        tours[index % num_robots].append(city)
    # Add depot at start and end
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    return tours

def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# --- Step 4: Shaking Procedure ---
def shake(tours, k):
    for _ in range(k):
        selected_tour = random.choice(tours)
        if len(selected_tour) <= 3:
            continue
        moved_city = random.choice(selected_tour[1:-1])
        selected_tour.remove(moved_city)
        target_tour = random.choice([t for t in tours if t != selected_tour])
        insert_pos = random.randint(1, len(target_tour)-1)
        target_tour.insert(insert_pos, moved_city)
    return tours

# --- Step 5: Sequential Variable Neighborhood Descent (Seq-VND) ---
# Implement a simple 2-opt as a local search improvement
def two_optimization(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if dist_matrix[tour[i]][tour[i+1]] + dist_matrix[tour[j]][tour[j+1]] > dist_matrix[tour[i]][tour[j]] + dist_matrix[tour[i+1]][tour[j+1]]:
                    tour[i+1:j+1] = reversed(tour[i+1:j+1])
                    improved = True
    return tour

def local_search(tours):
    return [two_optimization(tour) for tour in tours]

# --- Step 6: Integrated GVNS-like Procedure ---
num_robots = 2
tours = initial_solution(num_robots)
kmax = 4

for _ in range(10):  # simulation of iterations, equivalent to termination condition
    k = 1
    while k < kmax:
        new_tours = shake(tours, k)
        improved_tours = local_search(new_tours)
        if all(calculate_tour_cost(improved_tours[i]) < calculate_tour_cost(tours[i]) for i in range(num_robots)):
            tours = improved_tours
            k = 1
        else:
            k += 1

# Calculate costs and show results
tour_costs = [calculate_tour_cost(tour) for tour in tours]
max_cost = max(tour_costs)

for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")