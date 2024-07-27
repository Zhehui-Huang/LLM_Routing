import math

# Coordinates of the cities including the depot as city 0
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Nearest Neighbor heuristic to generate a tour starting and ending at the depot city 0
def nearest_neighbor_tour():
    num_cities = len(cities)
    visited = [False] * num_cities
    tour = [0]
    total_cost = 0
    current_city = 0
    visited[current_city] = True

    for _ in range(1, num_cities):
        next_city = None
        min_dist = float('inf')
        # Find the closest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                dist = distance(current_city, city)
                if dist < min_dist:
                    min_dist = dist
                    next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city

    # Return to the depot
    return_to_depot_cost = distance(current_city, 0)
    tour.append(0)
    total_cost += return_to_depot_cost

    return tour, total_cost

# Get the optimized tour and cost
tour, total_cost = nearest_neighbor_tour()

# Display the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")