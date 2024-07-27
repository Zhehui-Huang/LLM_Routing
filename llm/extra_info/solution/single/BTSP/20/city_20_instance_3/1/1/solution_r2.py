import math

# Define the cities' coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a matrix of distances between each pair of cities
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_tour():
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    total_cost = 0
    max_distance = 0

    # Start at the depot
    current_city = 0

    # Find the nearest unvisited city and go there till all cities are visited
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
        unvisited.remove(next_city)
        cost_to_next = dist_matrix[current_city][next_city]
        total_cost += cost_to_next
        max_distance = max(max_distance, cost_to_next)
        tour.append(next_city)
        current_city = next_city

    # Close the tour by returning to the depot
    final_cost_to_depot = dist_matrix[current_city][0]
    total_cost += final_cost_to_depot
    max_distance = max(max_distance, final_cost_to_depot)
    tour.append(0)

    return tour, total_cost, max_distance

# Execute the function to find the optimal tour
tour, total_cost, max_distance = find_tour()

# Print the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")