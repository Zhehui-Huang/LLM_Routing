import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate the distances matrix
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Simple greedy TSP implementation with optimizations
def greedy_tsp(distances, start):
    n = len(distances)
    visited = [False] * n
    tour = [start]
    total_cost = 0
    
    current_city = start
    visited[start] = True
    
    for _ in range(1, n):
        next_city = min((distances[current_city][j], j) for j in range(n) if not visited[j])[1]
        visited[next_to_visit_city] = True
        tour.append(next_city)
        total_cost += distances[current_city][next_city]
        current_city = next_city
    
    # Close the tour by returning to starting point
    total_cost += distances[current_city][start]
    tour.append(start)
    
    return tour, total_cost

tour, total_cost = greedy_tsp(distances, 0)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)