import math

# Coordinates of cities including the depot at index 0
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(start_index):
    """ Construct a tour using the nearest neighbor heuristic """
    num_cities = len(coordinates)
    unvisited = set(range(num_cities))
    unvisited.remove(start_index)
    tour = [start_index]
    current_index = start_index
    
    while unvisited:
        next_index = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_index], coordinates[x]))
        tour.append(next_index)
        unvisited.remove(next_index)
        current_index = nextxyz_index
        
    tour.append(start_index)  # Return to the starting city
    return tour

def calculate_tour_metrics(tour):
    """ Calculate the total travel cost and the maximum distance between consecutive cities in the tour """
    total_cost = 0
    max_leg_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
        if dist > max_leg_distance:
            max_leg_distance = dist
            
    return total_cost, max_leg_distance

tour = nearest_neighbor_tour(0)
total_cost, max_leg_distance = calculate_tour_metrics(tour)

# Print the results according to the format requirements
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))