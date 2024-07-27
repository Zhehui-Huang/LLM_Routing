import math
import sys

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbour_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # Start at the depot city
    total_cost = 0
    current_city = 0
    
    while len(tour) < n:
        nearest_city = None
        min_distance = sys.maxsize
        for i in range(1, n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    nearest_city = i
                    min_distance = distance
        if nearest_city is None:
            break
        visited[nearest_city] = True
        tour.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city
    
    # Return to the depot city
    total_cost += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    
    return tour, total_accost

# City coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Calculate the tour and cost
tour, total_cost = nearest_neighbour_tour(cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")