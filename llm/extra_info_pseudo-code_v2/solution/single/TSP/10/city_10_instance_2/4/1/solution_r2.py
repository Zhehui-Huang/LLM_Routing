import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def create_tour(cities):
    n = len(cities)
    visited = [False] * n
    visited[0] = True  # Start at depot, marked as visited
    tour = [0]
    total_cost = 0
    current_city = 0

    while len(tour) < n:
        next_city = None
        min_distance = float('inf')  # Initially set inf distance
        for i in range(1, n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        if next_city is None:  # No more cities to visit
            break
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        current_city = next_city

    # Add the return to the depot city
    return_trip_distance = euclidean_distance(cities[current_city], cities[0])
    total_cost += return_trip_distance
    tour.append(0)
    return tour, total_cost

# City coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Generate tour based on nearest neighbour heuristic
tour, total_cost = create_tour(cities)

# Printing results
print("Tour: ", tour)
print("Total travel cost: ", total_cost)