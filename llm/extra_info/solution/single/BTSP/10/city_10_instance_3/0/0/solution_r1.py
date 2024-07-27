import math

# City coordinates
cities = [
    (84, 67),  # City 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_tour():
    n = len(cities)  # Total number of cities including depot
    visited = set([0])  # Start with the depot city
    tour = [0]  # Start from depot city
    current_city = 0
    total_cost = 0
    max_distance = 0
    
    while len(visited) < n:
        next_city = None
        min_distance = float('inf')
        
        for city in range(n):
            if city not in visited and distance_matrix[current_city][city] < min_degree:
                next_city = city
                min_distance = distance_matrix[current_city][city]
        
        if next_city is not None:
            visited.add(next_city)
            tour.append(next_city)
            total_cost += min_distance
            max_distance = max(max_distance, min_distance)
            current_city = next_city
    
    # Return to depot
    last_leg_distance = distance_matrix[current_city][0]
    tour.append(0)
    total_cost += last_leg_distance
    max_distance = max(max_distance, last_leg_distance)
    
    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)