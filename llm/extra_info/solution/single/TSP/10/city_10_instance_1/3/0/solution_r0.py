import math
import itertools

# Coordinates for each city (indexed from 0 to 9)
positions = [
    (53, 68),  # depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_distance(tour):
    """Calculate the total distance of the given tour."""
    return sum(euclidean_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour) - 1))

def find_shortest_tour():
    """Find the shortest tour that visits all cities and return to the depot."""
    cities = list(range(1, len(positions)))  # excluding the depot city 0
    all_possible_tours = itertools.permutations(cities)
    
    shortest_tour = None
    min_distance = float('inf')
    
    for tour in all_possible_tours:
        current_tour = [0] + list(tour) + [0]  # add the depot to the beginning and the end
        current_distance = calculate_total_distance(current_tour)
        
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour
    
    return shortest_tour, min_distance

# Find the shortest tour and the corresponding travel cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))