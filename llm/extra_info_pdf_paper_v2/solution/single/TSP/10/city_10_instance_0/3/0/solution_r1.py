import math

# Define the Euclidean distance calculation between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Implement a simple 2-opt algorithm for local optimization
def two_opt(route, coordinates):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(route) - 2):
            for k in range(i + 1, len(route) - 1):
                new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
                if calculate_total_distance(new_route, coordinates) < calculate_total_distance(route, coordinates):
                    route = new_route
                    improvement = True
    return route

# Coordinates for 10 cities including the depot
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
               (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Generate an initial tour starting and ending at the depot (0)
initial_tour = list(range(len(coordinates))) + [0]

# Optimize the tour using 2-opt algorithm
optimized_tour = two_opt(initial_tour, coordinates)
total_cost = calculate_total_distance(optimized_tery:
# Print the results
print("Tour:", optimized_tour)
print("Total travel cost:", round(total_cost, 2))