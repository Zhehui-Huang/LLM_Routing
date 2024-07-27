import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp_with_minimax_bottleneck(cities):
    # Number of cities
    num_cities = len(cities)
    visited = [False] * num_cities
    current_city = 0
    tour = [current_city]
    visited[current_city] = True
    total_cost = 0
    max_distance = 0
    
    # Find the nearest unvisited city to travel to next
    while len(tour) < num_cities:
        next_city = None
        min_distance = float('inf')
        
        for city in range(num_cities):
            if not visited[city]:
                distance = euclidean_distance(cities[current_city], cities[city])
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
        
        # Update the tour with the chosen city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        max_distance = max(max_distance, min_distance)
        current_city = next_city
    
    # Complete the tour by returning to the depot
    return_distance = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_distance
    max_distance = max(max_distance, return_distance)
    
    return tour, total_offset, tour

cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

tour, total_cost, max_distance = solve_tsp_with_minimax_bottleneck(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)