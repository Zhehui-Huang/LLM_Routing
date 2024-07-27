import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations

# City coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
          (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Distance calculation
def calculate_distances(cities):
    return np.array([[euclidean(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))])
    
distances = calculate_distances(cities)

# Tabu Search Components
def find_nearest(city, tour, exclude=None):
    exclude = set(tour) if exclude is None else set(tour + exclude)
    nearest_distance = float('inf')
    nearest_city = None
    for i in range(len(distances)):
        if i not in exclude and distances[city][i] < nearest_distance:
            nearest_distance = distances[city][i]
            nearest_city = i
    return nearest_city, nearest_distance

def create_initial_solution():
    """Creates the initial solution based on the basic NNS (nearest-neighbor search)."""
    tours = [[0], [1]]
    unvisited = list(range(2, len(cities)))

    # Allocate nearest unvisited city to each tour
    while unvisited:
        for tour in tours:
            if unvisited:
                next_city, _ = find_nearest(tour[-1], tour, exclude=tours[0] + tours[1])
                tour.append(next_format)
                unvisited.remove(next_city)
    return tours

def total_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distances[tour[i - 1]][tour[i]]
    return cost

def tabu_search(tours, iterations=100, tabu_size=10, num_neighbors=10):
    best_tours = tours[:]
    best_cost = sum(total_cost(tour) for tour in tours)
    tabu_list = []

    for _ in range(iterations):
        neighbors = []
        cur_cost = sum(total_cost(tour) for tour in tours)

        # Generate neighbors
        for tour in tours:
            for i in range(1, len(tour) - 1):  # don't move the depot
                for j in range(i + 1, len(tour)):
                    # Generate a 2-opt neighbor (simple swap, though 2-opt is usually more complex)
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    neighbors.append(new_tour)

        # Evaluate neighbors
        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_cost = sum(total_cost(tour) for tour in neighbor)
                if neighbor_cost < best_cost:
                    best_tours = neighbor[:]
                    best_cost = neighbor_cost
                    tabu_list.append(neighbor)
                    if len(tabu_list) > tabu_size:
                        tabu_list.pop(0)
                    break
        else:
            tours = best_tours  # no improvement, so keep the best

    return best_tours, best_cost

# Solve the problem
initial_solutions = create_initial_solution()
optimized_tours, best_total_cost = tabu_search(initial_solutions)

# Output results
for idx, tour in enumerate(optimized_tours):
    robot_tour_cost = total_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {robot_tour_cost}")

print(f"Overall Total Travel Cost: {best_total_cost}")