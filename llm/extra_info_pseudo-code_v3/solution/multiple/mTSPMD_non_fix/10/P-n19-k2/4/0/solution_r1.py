import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
          (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Distance matrix
def get_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

dist_matrix = get_distance_matrix(cities)

def nearest_neighbor_solution(dist_matrix):
    n = len(dist_matrix)
    tours = [[0], [1]]
    unvisited = set(range(2, n))
    available = [[tour[-1]] for tour in tours]

    while unvisited:
        for a, available_cities in enumerate(available):
            closest_city = None
            closest_dist = float('inf')
            closest_tour_index = None
            
            for tour_index, city in enumerate(available_cities):
                for neighbor in unvisited:
                    if dist_matrix[city][neighbor] < closest_dist:
                        closest_city = neighbor
                        closest_dist = dist_matrix[city][neighbor]
                        closest_tour_index = tour_index
            
            if closest_city is not None:
                tours[a].append(closest_city)
                unvisited.remove(closest_city)
                available[a].append(closest_city)

    # Tours should end and start at individual depots
    for a, tour in enumerate(tours):
        tour_end = tour[-1]
        depot = tours[a][0]
        if tour_end != depot:
            tours[a].append(depot)
            tours[a].insert(0, depot)  # Ensure it starts from depot

    return tours

def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def tabu_search(initial_solutions, dist_matrix, iterations=100, tabu_tenure=10):
    best_solutions = initial_solutions[:]
    best_cost = sum(tour_cost(tour, dist_matrix) for tour in best_solutions)
    tabu_list = []

    for _ in range(iterations):
        for tour_index, tour in enumerate(best_solutions):
            for i in range(1, len(tour) - 2):
                for j in range(i + 1, len(tour) - 1):
                    # Perform 2-opt swap
                    new_tour = tour[:]
                    new_tour[i:j] = reversed(new_tour[i:j])
                    
                    candidate_solutions = best_solutions[:]
                    candidate_solutions[tour_index] = new_tour
                    candidate_cost = sum(tour_cost(t, dist_matrix) for t in candidate_solutions)
                    
                    if candidate_cost < best_cost and new_tour not in tabu_list:
                        best_solutions = candidate_solutions
                        best_cost = candidate_cost
                        tabu_list.append(new_tour)
                        if len(tabu_list) > tabu_tenure:
                            tabu_list.pop(0)
    
    return best_solutions, best_cost

initial_tours = nearest_neighbor_solution(dist_matrix)
optimized_tours, optimized_cost = tabu_search(initial_tours, dist_matrix)

# Output Results
for idx, tour in enumerate(optimized_tours):
    cost = tour_cost(tour, dist_matrix)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {optimized_cost}")