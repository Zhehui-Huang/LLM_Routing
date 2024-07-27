import math
from typing import List, Tuple

# City coordinates (based on the given problem data)
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def euclidean_distance(coords1: Tuple[int, int], coords2: Tuple[int, int]) -> float:
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

# Calculate distance matrix
distance_matrix = [
    [euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(len(city_coordinates))]
    for i in range(len(city_coordinates))
]

def nearest_neighbor_tour(start_city: int, cities: List[int]) -> List[int]:
    """Construct a tour using the nearest neighbor heuristic starting from the given city."""
    unvisited = set(cities)
    current_city = start_city
    tour = [current_city]
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to the depot
    return tour

# Assign cities to robots, excluding the depot city which is city 0
cities = list(range(1, len(city_coordinates)))
tours = [nearest_neighbor_tour(0, cities)]

# Function to calculate total travel cost for a tour
def calculate_tour_cost(tour: List[int]) -> float:
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Display results
total_overall_cost = 0
print("Tours analysis:")
for i, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    total_overall_cost += cost

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")