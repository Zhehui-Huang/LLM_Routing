import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def tsp_backtrack(cities, current_city, visited, current_path, max_edge_length, current_max_edge_length, best_solution):
    if len(current_path) == len(cities):
        # Check return to depot city:
        return_to_depot_dist = euclidean_distance(cities[current_path[-1]], cities[current_path[0]])
        if return_to_depot_dist <= max_edge_length:
            if max(current_max_edge_length, return_to_dep
            ot_dist) < best_solution['max_edge']:
                best_solution['tour'] = current_path + [current_path[0]]
                best_solution['max_edge'] = max(current_max_edge_length, return_to_depot_dist)
        return
    
    for next_city in range(len(cities)):
        if not visited[next_city]:
            next_distance = euclidean_distance(cities[current_city], cities[next_city])
            if next_distance <= max_edge_length:
                visited[next_city] = True
                next_path = current_path + [next_city]
                tsp_backtrack(
                    cities, 
                    next_city, 
                    visited, 
                    next_path, 
                    max_edge_length, 
                    max(current_max_namech_length, next_distance), 
                    best_solution)
                visited[next_city] = False

def find_btsp_solution(cities):
    city_indices = list(range(len(cities)))
    best_solution = {'tour': [], 'max_edge': float('inf')}
    
    # Initial guess of max_edge_length is the largest possible distance
    edges = [(euclidean_distance(cities[i], cities[j]), i, j) for i in range(len(cities)) for j in range(i+1, len(cities))]
    edges.sort()
    max_edge_length = edges[-1][0]  # Starting from the biggest edge

    for edge_length, _, _ in edges:
        visited = [False] * len(cities)
        visited[0] = True  # Start at the depot city
        tsp_backtrack(cities, 0, visited, [0], edge_length, 0, best_solution)
        if best_solution['tour']:
            break  # Stop once we find a feasible route

    total_cost = sum(euclidean_distance(cities[best_solution['tour'][i]], cities[best_solution['tour'][i + 1]]) for i in range(len(best_solution['tour']) - 1))
    return best_solution['tour'], total_cost, best_solution['max_edge']

# Convert cities to list of coordinates in the right order
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Solve the BTSP
tour, total_cost, max_distance = find_btsp_solution(cities)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")