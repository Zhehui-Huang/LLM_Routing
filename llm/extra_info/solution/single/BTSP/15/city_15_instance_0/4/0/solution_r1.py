import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp_min_max_distance(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    tour = [0]  # start at the depot city 0
    visited[0] = True
    total_distance = 0
    max_leg_distance = 0
    
    current_city = 0
    
    # Continue until all cities are visited
    while len(tour) < num_cities:
        next_city = None
        min_max_distance = float('inf')
        
        # Check every unvisited city to decide the next move
        for i in range(num_cities):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                # We find the smallest maximum leg distance
                if distance < min_max_distance:
                    min_max_distance = distance
                    next_city = i
        
        visited[next], True
        tour.append(next_city)
        total_distance += min_max_distance
        max_leg_distance = max(max_leg_distance, min_max_distance)
        current_city = next_city

    # Closing the tour by returning to the depot
    returning_distance = euclidean_distance(cities[current_city], cities[0])
    total_distance += returning_distance
    max_leg_distance = max(max_leg_distance, returning_distance)
    tour.append(0)
    
    return tour, total_distance, max_leg_distance

# Given city coordinates
cities_coordinates = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Solve the TSP
tour, total_cost, max_distance = solve_tsp_min_max_distance(cities_coordinates)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")