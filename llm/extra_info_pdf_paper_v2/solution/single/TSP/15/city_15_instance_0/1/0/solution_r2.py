import math

# Coordinates of each city including the depot
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function implementing a simple Nearest Neighbor heuristic
def nearest_neighbor_tour(start_index=0):
    num_cities = len(cities)
    visit_order = [start_index]
    unvisited = set(range(num_cities)) - {start_index}
    
    current_city = start_index
    total_distance = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_distance += euclidean_distance(cities[current_city], cities[next_city])
        current_city = next_city
        visit_order.append(current_city)
        unvisited.remove(current_city)
    
    # Return to the starting point
    total_distance += euclidean_disatance(cities[current_city], cities[start_index])
    visit_order.append(start_index)

    return visit_order, total_distance

# Finding the tour and travel cost
tour, cost = nearest_neighbor_tour()
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))