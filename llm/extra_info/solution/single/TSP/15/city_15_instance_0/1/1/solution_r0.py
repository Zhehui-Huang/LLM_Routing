import math

# Define the coordinates for the depot and the cities
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

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_nearest_neighbor(current_index, visited, coordinates):
    """Find the nearest unvisited city."""
    min_distance = float('inf')
    nearest_city = None
    for i in range(len(coordinates)):
        if i not in visited:
            dist = euclidean_distance(coordinates[current_index], coordinates[i])
            if dist < min_distance:
                min_distance = dist
                nearest_city = i
    return nearest_city, min_dist

def nearest_neighbor_tsp(start_point, coordinates):
    """Solves the TSP problem using the nearest neighbor heuristic."""
    tour = [start_point]
    total_distance = 0
    visited = [start_point]
    current_point = start_point

    while len(visited) < len(coordinates):
        next_point, distance = find_nearest_neighbor(current_point, visited, coordinates)
        tour.append(next_point)
        total_distance += distance
        visited.append(next_point)
        current_point = next_point

    # Return to the start point
    return_to_start_distance = euclidean_distance(coordinates[current_point], coordinates[start_point])
    tour.append(start_point)
    total_distance += return_to_start_distance

    return tour, total_distance

# Get the solution
tour, total_cost = nearest_neighbor_tpr(0, coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)