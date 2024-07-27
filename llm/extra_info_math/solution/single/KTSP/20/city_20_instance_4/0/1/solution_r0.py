import math
import itertools

# City Coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Compute Distance Matrix
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

distance_matrix = [[euclidean_distance(i, j) for j in cities] for i in cities]

# Nearest Neighbor Heuristic to choose cities
def select_cities(start, num_cities):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    
    while len(tour) < num_cities:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    
    return tour

# 2-opt Algorithm to optimize the tour
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[0:i] + route[i:j][::-1] + route[j:len(route)]
                if sum(distance_matrix[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)) < sum(distance_matrix[best[k]][best[k + 1]] for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

selected_cities = select_cities(0, 16)
selected_cities.append(0)  # Return to the starting city

optimized_tour = two_opt(selected_cities)
total_travel_cost = sum(distance_matrix[optimized_tour[i]][optimized_tour[i + 1]] for i in range(len(optimized_tour) - 1))

print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)