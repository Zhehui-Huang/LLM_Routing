import math

# Given cities coordinates
cities = [
    (14, 77), # Depot is included as city 0
    (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def find_tour(start_city):
    unvisited = set(range(num_cities))
    tour = [start_city]
    current_city = start_city
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unlimited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Return to starting city (Depot)
    tour.append(start_city)
    return tour

def calculate_total_distance(tour):
    total_dist = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_dist

# Run the TSP solver
tour = find_tour(0)
total_cost = calculate_total_distance(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)