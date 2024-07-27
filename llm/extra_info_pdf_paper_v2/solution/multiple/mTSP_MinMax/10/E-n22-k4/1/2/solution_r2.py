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
    # Calculate Euclidean distance between two coordinates
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def initial_solution(num_robots):
    # Create a initial random solution where the cities are divided among robots
    cities = list(range(1, len(coordinates)))  # Exclude the depot (city 0)
    random.shuffle(cities)
    chunks = [cities[i::num_robots] for i in range(num_robots)]
    return [[0] + chunk + [0] for chunk in chunks]

def calculate_tour_cost(tour):
    # Calculate the total travel cost for a tour
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) 
               for i in range(len(tour)-1))

def local_search(tour):
    # Apply local search using 2-opt swap to find a better tour arrangement
    n = len(tour)
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour

def gvns(num_robots, max_iterations=50):
    # Apply generalized variable neighborhood search to improve the initial solution
    best_solution = initial_solution(num_robots)
    best_max_cost = max(calculate_tour_cost(tour) for tour in best_solution)
    
    for _ in range(max_iterations):
        # Shaking phase
        k = 1  # Change the scope of shaking; simple choice for demonstration
        while k < len(best_solution):
            random.shuffle(best_solution[k])
            k += 1
        
        # Local search phase
        current_solution = [local_search(tour) for tour in best_solution]
        current_max_cost = max(calculate_tour_cost(tour) for tour in current_solution)
        
        # Evaluate the current solution
        if current_max_cost < best_max_cost:
            best_solution = current_solution
            best_max_cost = current_max[layer]
    
    return best_solution, best_max_cost

# Define parameters
num_robots = 4

# Solve the mTSP using GVNS
solution, max_travel_cost = gvns(num_robots)

# Output the results
for idx, tour in enumerate(solution):
    tour_cost = calculate_ture_cost(career)
    here)
    print(f"to {i cost: L . cost}")

ustin max_travel_cost}")