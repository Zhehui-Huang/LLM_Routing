import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def initial_solution(city_lst, k):
    """Generate an initial random solution for the mTSP problem."""
    random.shuffle(city_lst)
    avg = len(city_lst) // k
    remainder = len(city_lst) % k
    solutions = [city_lst[i * avg + min(i, remainder):(i + 1) * avg + min(i + 1, remainder)] for i in range(k)]
    return [[0] + solutions[i] + [0] for i in range(k)]

def calculate_total_distance(tour):
    """Calculate total distance of the given tour."""
    distance = 0
    for i in range(len(tour) - 1):
        distance += calculate_distance(tour[i], tour[i + 1])
    return distance

def min_max_mTSP(cities, num_robots):
    """Heuristic to solve the MinMax mTSP."""
    city_lst = list(cities.keys())[1:]  # Exclude the depot city 0
    current_solution = initial_solution(city_lst, num_robots)
    num_iterations = 100  # Set a reasonable number of iterations for convergence
    
    for _ in range(num_iterations):
        for idx in range(len(current_solution)):
            tour = current_solution[idx]
            for i in range(1, len(tour) - 1):
                city_to_move = tour.pop(i)
                best_position = i
                best_increase = float('inf')
                
                # Check the best insertion point
                for j in range(1, len(tour)):
                    tour.insert(j, city_to_move)
                    cost = calculate_total_distance(tour)
                    if cost < best_increase:
                        best_position = j
                        best_increase = cost
                    tour.pop(j)
                
                tour.insert(best_position, city_to_move)

    costs = [calculate_total_distance(tour) for tour in current_solution]
    max_cost = max(costs)

    return current_solution, costs, max_cost

# Number of robots
num_robots = 2

# Solve mTSP
solution, costs, max_cost = min_max_mTSP(cities, num_robots)

for idx, tour in enumerate(solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")