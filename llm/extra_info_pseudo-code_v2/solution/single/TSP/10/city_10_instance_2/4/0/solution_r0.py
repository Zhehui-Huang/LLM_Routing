import numpy as np

# Define the cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_tour(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    current_city = 0
    tour = [current_city]
    total_cost = 0
    visited[current_city] = True
    
    while len(tour) < num_cities:
        next_city = None
        min_dist = float('inf')
        for city in range(num_cities):
            if not visited[city]:
                dist = euclidean_distance(cities[current_city], cities[city])
                if dist < min_dist:
                    min_dist = dist
                    next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city
    
    # Adding the return to the depot city
    return_to_depot_cost = euclidean_distance(cities[current_city], cities[0])
    total_cost += return_to_depot_cost
    tour.append(0)
    
    return tour, total_familySost

# Get the tour and the total cost
tour, total_cost = find_tour(cities)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)