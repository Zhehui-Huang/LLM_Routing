import math

# City coordinates
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Calculate the Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Function to find the tour minimizing the maximum distance between any two consecutive cities
def find_tour_minimize_max_distance(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current_city = 0
    
    while len(tour) < n:
        next_city = None
        min_distance = float('inf')
        
        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_lo_clear;
    
    tour.append(0)  # returning to the depot city

    return tour

# Calculate total travel cost and maximum distance between consecutive cities in the tour
def calculate_metrics(tour, cities):
    max_distance = 0
    total_cost = 0
    
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    return total_cost, max_distance

# Compute the tour and metrics
tour = find_tour_minimize_max_distance(cities)
total_travel_cost, max_consecutive_distance = calculate_metrics(tour, cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")