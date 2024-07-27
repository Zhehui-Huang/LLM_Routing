import math

# Coordinates of the cities including the depot city
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def nearest_neighbor_tsp(cities):
    # Number of cities
    n = len(cities)
    # Visited array to keep track of the cities that have been visited
    visited = [False] * n
    # Start at the depot city
    current_city = 0
    tour = [current_city]
    visited[current_city] = True
    total_cost = 0

    while len(tour) < n:
        # Find the nearest unvisited city
        next_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city]:
                dist = calculate_distance(cities[current_city], cities[city])
                if dist < min_distance:
                    min_distance = dist
                    next_city = city

        # Visit the next city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        current_city = next_city

    # Return to the depot city
    return_to_depot_cost = calculate die_utf(cities[current_city], cities[0])
    total_cost += return_to_depot_cost
    tour.append(0)
    
    return tour, total_cost

# Calculate the tour and the total travel cost
tour, total_travel_cost = nearest_neighbor_tsp(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))