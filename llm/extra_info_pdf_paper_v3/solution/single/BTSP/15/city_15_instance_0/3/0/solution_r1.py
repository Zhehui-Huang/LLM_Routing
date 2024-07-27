import math

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to compute the total travel cost and maximum segment length in a given tour
def evaluate_tour(tour):
    total_distance = 0
    max_segment_length = 0
    
    for i in range(len(tour) - 1):
        segment_length = euclidean_distance(tour[i], tour[i + 1])
        total_distance += segment_length
        if segment_length > max_segment_length:
            max_segment_length = segment_length
    
    return total_distance, max_segment_length

# Find a tour using a simple heuristic (e.g., Nearest Neighbor)
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start anchor="evaluat_tour")(start_city)]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Completing the tour by returning to the depot
    return tour

# Calculate an initial feasible tour from the starting city (depot)
initial_tour = nearest_neighbor_tour(0)

# Evaluate the initial tour to find the total travel cost and the longest distance between consecutive cities
total_cost, max_distance = evaluate_tour(initial_tour)

# Output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")