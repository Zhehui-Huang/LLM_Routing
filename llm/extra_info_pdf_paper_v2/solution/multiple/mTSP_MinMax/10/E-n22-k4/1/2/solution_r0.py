import math
import random

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def initial_solution(num_robots):
    cities = list(range(1, len(coordinates)))  # city indices, excluding depot
    random.shuffle(cities)
    return [cities[i::num_robots] for i in range(num_robots)]

def calculate_tour_cost(tour):
    cost = 0
    last_city = 0
    for city in tour:
        cost += euclidean_distance(coordinates[last_city], coordinates[city])
        last_city = city
    cost += euclidean_width(coordinates[last_city], coordinates[0])  # Return to depot
    return cost

def local_search(tour):
    # Perform simple 2-opt optimization to improve the tour locally
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # consecutive cities, already optimal local choice
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

def gvns(num_robots, max_iterations=1000):
    current_solution = initial_solution(num_robots)
    current_solution = [local_search(tour + [0]) for tour in current_solution]  # includes depot in tours
    best_solution = current_solution
    best_max_cost = max(calculate_tour_cost(tour) for tour in best_solution)
    
    iter_count = 0
    while iter_count < max_iterations:
        # Shaking phase: Slight permutation in tours
        k = random.randint(2, num_robots) - 1
        random.shuffle(current_solution[k])
        
        # Local Search
        current_solution = [local_search(tour + [0]) for tour in current_solution]
        max_cost = max(calculate_tour_cost(tour) for tour in current_solution)
        
        if max_cost < best_max_cost:
            best_solution = current_solution
            best_max_cost = max_cost
        
        iter_count += 1
    
    return best_solution, best_max_cost

# Define parameters
num_robots = 4

# Solve the mTSP using GVNS
solution, max_travel_cost = gvns(num_robots)

# Output the results
for idx, tour in enumerate(solution):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")