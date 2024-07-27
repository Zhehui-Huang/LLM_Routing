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
    tours = [cities[i::num_robots] for i in range(num_robots)]
    return [[0] + tour + [0] for tour in tours]  # include depot as start and end

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def local_search(tour):
    # Perform simple 2-opt optimization to improve the tour locally
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
        tour = best_tour
    return tour

def gvns(num_robots, max_iterations=100):
    current_solution = initial_solution(num_robots)
    current_solution = [local_search(tour) for tour in current_solution]
    best_solution = current_solution
    best_max_cost = max(calculate_tour_cost(tour) for tour in best_solution)
    
    for _ in range(max_iterations):
        # Shaking phase: Modify a random tour slightly
        tour_index = random.randint(0, num_robots - 1)
        new_tour = local_search(initial_solution(1)[0])
        new_solution = best_solution[:]
        new_solution[tour_index] = new_tour

        # Local search on new solution
        new_solution = [local_search(tour) for tour in new_solution]
        new_max_cost = max(calculate_tour_cost(tour) for tour in new_solution)
        
        # Acceptance criterium: Check if the maximum cost of the new solution is lower
        if new_max_print_cost < best_max_cost:
            best_solution = new_solution
            best_max_print_cost = new_max_print_cost
    
    return best_solution, best_max_cost;

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