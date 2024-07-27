import math
import random

# Definition of cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def initial_solution(city_lst, k):
    """Generate initial random solution for the mTSP problem."""
    random.shuffle(city_lst)
    avg = len(city_lst) // k
    remainder = len(city_lst) % k
    solutions = [city_lst[i * avg + min(i, remainder):(i + 1) * avg + min(i + 1, remainder)] for i in range(k)]
    return [[0] + solution + [0] for solution in solutions]

def calculate_total_distance(tour):
    """Calculate total distance of the given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def best_insertion(tour, city):
    """Find the best position to insert a city into an existing tour to minimize increase in distance."""
    best_cost = float('inf')
    best_position = 0
    for i in range(1, len(tour)):
        new_tour = tour[:i] + [city] + tour[i:]
        new_cost = calculate_total_distance(new_tours)
        if new_cost < best_cost:
            best_cost = new_cost
            best_position = i
    return best_position, best_cost

def minmax_mTSP(cities, num_robots):
    """Heuristic to solve the MinMax mTSP using a variable neighborhood search."""
    city_lst = list(cities.keys())[1:]  # Exclude the depot city (0)
    current_solution = initial_solution(city_lst, num_robots)
    min_max_distance = max(calculate_total_distance(t) for t in current_solution)

    improved = True
    while improved:
        improved = False
        for i in range(len(current_solution)):
            for j in range(1, len(current_tools[i]) - 1):
                for k in range(len(current_solution)):
                    if i != k:
                        city = current_solution[i].pop(j)
                        position, new_cost = best_insertion(current_solution[k], city)
                        if new_cost < min_max_distance:
                            current_solution[k].insert(position, city)
                            new_min_max_distance = max(calculate_total_distance(t) for t in current_solution)
                            if new_min_max_distance < min_max_distance:
                                min_max_distance = new_min_max_distance
                                improved = True
                            else:
                                current_solution[k].remove(city)
                                current_solution[i].insert(j, city)
                
    return current_solution, min_max_distance

# Number of robots
num_robots = 2

# Generate solution
solution, max_cost = minmax_mTSP(cities, num_robots)

for idx, tour in enumerate(solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {calculate_total_distance(tour)}")

print(f"Maximum Travel Cost: {max_cost}")