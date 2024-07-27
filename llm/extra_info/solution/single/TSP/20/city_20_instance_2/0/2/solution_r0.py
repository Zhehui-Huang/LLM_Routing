import math

# Define the coordinates of each city including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # Start at the depot city 0
    current_city = 0
    total_cost = 0

    while len(tour) < n:
        nearest_city = None
        min_distance = float('inf')
        for i in range(1, n):  # Start from 1 to avoid selecting the depot initially
            if not visited[i]:
                distance = calculate_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    nearest_city = i
                    min_distance = distance
        visited[nearest_city] = True
        tour.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city

    # Return to depot
    back_to_depot_distance = calculate_distance(cities[current_city], cities[0])
    total_cost += back_to_depot_distance
    tour.append(0)  # Complete the tour by returning to the starting point

    return tour, total_cost

# Compute the shortest tour using the Nearest Neighbor heuristic
tour, total_cost = find_shortest_tour(cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")