import math

# City coordinates indexed from 0 to 9 (Depot at index 0)
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
               (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate initial tour with a greedy approach
def greedy_tour(coordinates):
    start = 0
    tour = [start]
    unvisited = list(range(1, len(coordinates)))
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[tour[-1]], coordinates[x]))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)  # complete the tour by returning to the depot
    return tour

# Function to execute 2-opt swap
def perform_two_opt(tour, coordinates):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour)-2):
            for k in range(i+1, len(tour)-1):
                new_route = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
                if calculate_total_distance(new_route, coordinates) < calculate_total_distance(tour, coordinates):
                    tour = new_route
                    improvement = True
    return tour

# Calculate total distance for the tour
def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

# Apply Greedy and 2-OPT optimization to find the shortest tour
initial_tour = greedy_tour(coordinates)
optimized_tour = perform_two_opt(initial_tour, coordinates)
total_cost = calculate_total_distance(optimized_tour, coordinates)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)