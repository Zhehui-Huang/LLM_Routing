import math

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_tour():
    n = len(cities)
    visited = [False] * n
    tour = [0]  # Start tour at depot city index 0
    visited[0] = True
    current_city_index = 0
    total_cost = 0
    max_distance = 0
    
    while len(tour) < n:
        next_city_index = None
        min_dist = float('inf')
        
        # Find the nearest non-visited city
        for i in range(n):
            if not visited[i]:
                dist = euclidean_distance(cities[current_city_index], cities[i])
                if dist < min_dist:
                    min_dist = dist
                    next_city_index = i
        
        # Update the tour and metrics
        tour.append(next_city_index)
        visited[next_city_index] = True
        total_cost += min_dist
        max_distance = max(max_distance, min_dist)
        current_city_index = next_city_index
    
    # Close the tour by returning to the depot
    return_to_depot = euclidean_distance(cities[current_city_index], cities[0])
    tour.append(0)
    total_cost += return_to_depot
    max_distance = max(max_distance, return_to_depot)
    
    return tour, total_cost, max_distance

# Calculate the tour, total cost, and max distance
tour, total_travel_cost, max_consecutive_distance = find_tour()

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)