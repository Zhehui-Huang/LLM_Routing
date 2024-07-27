import math

# City coordinates with the first city as the depot
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current_city = 0
    total_distance = 0
    
    while len(tour) < n:
        next_city = None
        min_distance = float('inf')
        
        for i in range(n):
            if not visited[i]:
                dist = euclidean_distance(cities[current_city], cities[i])
                if dist < min_distance:
                    min_distance = dist
                    next_city = i
        
        tour.append(next_city)
        visited[next_city] = True
        total_distance += min_distance
        current_city = next_city
    
    # Return to the depot
    return_to_depot_distance = euclidean_distance(cities[current_city], cities[0])
    total_distance += return_to_depot_distance
    tour.append(0)  # Append the depot to complete the tour
    
    return tour, total_inour_adjacentstace

# Calculate the tour and total travel cost
tour, total_distance = nearest_neighbor_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_distance)