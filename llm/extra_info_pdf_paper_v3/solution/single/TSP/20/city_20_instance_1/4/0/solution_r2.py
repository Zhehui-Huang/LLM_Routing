import math

# Define the cities' coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(start, cities):
    """Return a tour starting from a given city using the nearest neighbor heuristic."""
    visited = set([start])
    tour = [start]
    current_city = start
    
    while len(visited) < len(cities):
        next_city, min_distance = min(
            ((city, euclidean_distance(cities[current_city], cities[city]))
             for city in cities if city not in visited),
            key=lambda x: x[1]
        )
        
        visited.add(next_city)
        tour.append(next_city)
        current_city = next_city
    
    # Closing the tour by returning to the start city
    tour.append(start)
    return tour

def calculate_tour_cost(tour, cities):
    """Calculate the total cost of a tour based on Euclidean distances."""
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return total_cost

# Compute the tour and cost
tour = nearest_neighbor_tour(0, cities)
tour_cost = calculate_tour_cost(tour, cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")