import math

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Euclidean distance calculator
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Construct the distance matrix
n = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Heuristic: Greedy approach to find the next closest unvisited city
def find_path():
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    
    max_distance = 0
    total_distance = 0
    
    while unvisited:
        # Find the nearest unvisited city
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        travel_dist = distance_matrix[current_city][next_city]
        
        # Append to tour
        tour.append(next_city)
        total_distance += travel_dist
        max_distance = max(max_distance, travel_dist)
        
        # Update the current city and mark as visited
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to the starting city (depot)
    return_to_depot = distance_matrix[current_city][0]
    tour.append(0)
    total_distance += return_to_depot
    max_distance = max(max_distance, return_to_depot)
    
    return tour, total_distance, max_distance

# Get the generated tour, total travel cost and the maximum leg distance
tour, total_cost, max_leg_distance = find_path()

# Print outputs
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))