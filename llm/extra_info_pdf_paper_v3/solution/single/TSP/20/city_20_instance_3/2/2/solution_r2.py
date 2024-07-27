import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tsp(start, cities):
    n = len(cities)
    visit_order = [start]
    visited = set(visit_order)
    total_cost = 0

    current = start
    while len(visit_order) < n:
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if i not in visited:
                dist = euclidean_distance(cities[current], cities[i])
                if dist < min_dist:
                    min_dist = dist
                    next_city = i
        visit_order.append(next_city)
        visited.add(next_city)
        total_cost += min_dist
        current = next_city

    # Return to start city
    total_cost += euclidean_distance(cities[current], cities[start])
    visit_order.append(start)

    return visit_order, total_cost

# Define the cities with coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Start from depot (index 0)
tour, cost = nearest_neighbor_tsp(0, cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))