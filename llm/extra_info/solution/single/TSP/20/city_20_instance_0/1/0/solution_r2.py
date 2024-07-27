import math

# Cities coordinates
cities_coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the closest unvisited city
def find_closest(current_city, visited):
    closest_city = None
    min_dist = float('inf')
    for city in range(1, 20):  # start from 1 since 0 is depot
        if city not in visited:
            dist = euclidean_distance(current_city, city)
            if dist < min_dist:
                min_dist = dist
                closest_city = city
    return closest_city, min_dist

# Greedy Nearest Neighbor algorithm
def greedy_nearest_neighbor():
    tour = [0]  # Start at the depot city
    total_cost = 0
    visited = set(tour)
  
    current_city = 0
    while len(visited) < 20:
        next_city, cost = find_closest(current_city, visited)
        tour.append(next_city)
        visited.add(next_city)
        total_cost += cost
        current_city = next_city
    
    # Return to the depot city
    return_to_depot_cost = euclidean_distance(current_city, 0)
    tour.append(0)  # End at the depot city
    total_cost += return_to_depot_cost
    
    return tour, total_cost

# Compute the tour and total travel cost using Greedy Nearest Neighbor
tour, total_travel_cost = greedy_nearest_neighbor()

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_travel_tcost,2))