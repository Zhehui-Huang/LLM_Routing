import math
from typing import Tuple, List, Union

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def construct_tour(cities: List[Tuple[int, int]]) -> Tuple[List[int], float, float]:
    num_cities = len(cities)
    unvisited = set(range(1, num_cities))
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # Complete the tour by returning to the depot
    
    # Calculate the total cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_cost, max_distance

# Coordinates given (index matches city number)
cities_coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Solve the problem
tour, total_cost, max_distance = construct_tour(cities_coordinates)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")