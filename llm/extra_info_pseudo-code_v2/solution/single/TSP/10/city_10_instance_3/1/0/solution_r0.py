import math
import sys

# Define the cities: Index and coordinates
cities = [
    (84, 67),  # City 0: Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Implementation of a Greedy Nearest Neighbor approach to find a tour
def find_tour(cities):
    n = len(cities)
    unvisited = list(range(1, n))  # Start from city 1 to n-1 as city 0 is the depot
    tour = [0]  # Start the tour from the depot
    total_cost = 0
    
    current_city = 0
    while unvisited:
        next_city = None
        min_distance = sys.maxsize
        for city in unvisited:
            dist = calculate_distance(cities[current_city], cities[city])
            if dist < min_distance:
                min_distance = dist
                next_city = city
        
        tour.append(next_node)
        unvisited.remove(next_city)
        total_cost += min_distance
        current_city = next_city
        
    # Return to depot
    return_cost = calculate_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_cost
    
    return tour, total_cost

# Compute the tour and the total cost
tour, total_cost = find_tour(cities)

# Output the results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')