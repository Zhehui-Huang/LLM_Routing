import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # start at the depot city 0
    current_city = 0
    total_cost = 0
    
    visited[0] = True  # Mark the depot as visited
 
    for _ in range(n - 1):
        next_city = None
        min_distance = float('inf')
        
        for city in range(n):
            if not visited[city]:
                distance = euclidean_distance(cities[current_city], cities[city])
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
        
        tour.append(next_city)
        visited[next_city] = True
        total_cost += min_distance
        current_city = next_city
        
    # Add the return trip to the depot
    total_cost += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)  # complete the tour by returning to the depot
    
    return tour, total_cost

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Convert dictionary to list for easier indexing
city_coordinates = [cities[i] for i in range(len(cities))]

# Compute the shortest tour
tour, total_cost = find_shortest_tour(city_coordinates)

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)