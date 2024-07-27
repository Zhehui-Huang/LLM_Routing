import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour: List[int], cities: List[Tuple[int, int]]) -> float:
    total_distance = 0.0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def nearest_neighbor(cities: List[Tuple[int, int]], start_index: int) -> List[int]:
    n = len(cities)
    unvisited = set(range(n))
    current_city = start_index
    tour = [current_city]
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_index)  # return to the depot city
    return tour

def two_opt(tour: List[int], cities: List[Tuple[int, int]]) -> List[int]:
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # consecutive edges are not viable
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(new_tour, cities) < calculate_total_distance(tour, cities):
                    tour = new_tour
                    improved = True
        if improved:
            break
    return tour

# Coordinates of the cities including the depot city
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Initial solution using nearest neighbor starting from the depot city (index 0)
initial_tour = nearest_neighbor(cities, 0)

# Improve the tour using the 2-opt heuristic
optimized_tour = two_opt(initial_tour, cities)

# Calculate the total cost of the optimized tour
total_travel_cost = calculate_total_distance(optimized_tour, cities)

# Output the results as required
print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_post)