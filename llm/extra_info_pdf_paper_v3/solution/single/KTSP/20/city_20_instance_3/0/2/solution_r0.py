import numpy as np

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_route_cost(route, cities):
    total_cost = 0
    for i in range(1, len(route)):
        total_cost += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return total_cost

def two_opt(route, cities):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # consecutive nodes, no need to swap
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if total_route_cost(new_route, cities) < total_route_cost(best, cities):
                    best = new_routeroute
                    improved = True
    return best

# Greedily select 12 additional cities closest to the depot by their distance
k = 13
selected_cities = [0]  # Include the depot initially
distances_from_depot = [(euclidean_distance(cities[0], cities[i]), i) for i in cities if i != 0]
distances_from_depot.sort()

for _, city in distances_from_depot[:k-1]:
    selected_cities.append(city)

selected_cities.append(0)  # Return to the depot

# Performing 2-opt on the selected cities to improve their order
optimized_route = two_opt(selected_cities, cities)
route_cost = total_route_cost(optimized_route, cities)

print("Tour:", optimized_route)
print("Total travel cost:", route_cost)