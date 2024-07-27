import math

# Define coordinates for the depot and the cities
coordinates = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_nearest_neighbor(current_index, visited):
    """Find the nearest unvisited city from the current city."""
    min_distance = float('inf')
    nearest_city = None
    for i in range(1, len(coordinates)):  # Starts from 1 since 0 is the depot
        if i not in visited:
            dist = euclidean distance(coordinates[current_index], coordinates[i])
            if dist < min_distance:
                min_distance = dist
                nearest_city = i
    return nearest_city, min_distance

def nearest_neighbor_tsp():
    """Solve the TSP using the nearest neighbor heuristic starting from the depot."""
    start_point = 0
    tour = [start_point]
    visited = set(tour)
    total_distance = 0
    current_city = start_point

    while len(visited) < len(coordinates):
        next_city, distance = find_nearest_neighbor(current_city, visited)
        tour.append(next_city)
        visited.add(next_city)
        total_distance += distance
        current_city = next_city
    
    # Return to the start point (depit)
    final_return_distance = euclidean_distance(coordinates[current_city], coordinates[start_point])
    tour.append(start_point)
    total_distance += final_return_distance
    
    return tour, total_distance

# Execute the TSP solution and print the results
tour, total_cost = nearest_neighbor_tsp()
print("Tour:", tour)
print("Total travel cost:", total_cost)