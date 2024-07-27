import math
import random

# Coordinates of all cities including the depot
cities = [
    (30, 40),  # Depot
    (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), 
    (58, 27), (37, 69), (61, 33), (62, 63), 
    (63, 69), (45, 35)
]

def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Assign cities to robots
def assign_cities(num_robots):
    num_cities = len(cities) - 1
    city_indices = list(range(1, num_cities + 1))
    random.shuffle(city_indices)
    return [city_indices[i::num_robots] for i in range(num_robots)]

# Simple nearest neighbor heuristic to create initial tour for each robot
def create_tour(assigned_cities):
    tour = [0]  # start at depot
    unvisited = set(assigned_cities)
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    tour.append(0)  # return to depot
    return tour

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i == 1 and j == len(tour) - 2:
                    continue  # Don't reverse the path from depot back to itself
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Run mTSP
def solve_mtsp(num_robots):
    assigned_cities = assign_cities(num_robots)
    tours = [create_tour(assign) for assign in assigned_cities]
    optimized_tours = [two_opt(tour) for tour in tours]
    costs = [calculate_tour_cost(tour) for tour in optimized_tours]
    
    total_cost = sum(costs)
    results = []
    for i, (tour, cost) in enumerate(zip(optimized_tours, costs)):
        results.append(f"Robot {i} Tour: {tour}")
        results.append(f"Robot {i} Total Travel Cost: {cost:.2f}")
    results.append(f"Overall Total Travel Cost: {total_cost:.2f}")
    
    return "\n".join(results)

# Execute for 2 robots
result = solve_mtsp(2)
print(result)