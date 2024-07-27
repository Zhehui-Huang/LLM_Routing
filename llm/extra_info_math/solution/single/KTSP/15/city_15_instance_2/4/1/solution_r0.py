import math
from itertools import combinations

# Define functions to calculate the Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Define all cities with their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate tour distance
def tour_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

# Function to find the shortest tour through the cities, starting and finishing at depot city 0
def find_shortest_tour():
    # What we're looking for is the shortest route that includes exactly 8 cities
    minimum_distance = float('inf')
    best_tour = []
    
    # Generate all combinations of 7 cities (excluding the depot, which must be included)
    for subset in combinations(range(1, 15), 7):  # Choose 7 cities because depot city 0 is a must-have
        current_tour = [0] + list(subset) + [0]  # Start and end at the depot city
        
        # We need to determine the order of visit in the best way
        # Let's use a simple nearest neighbor heuristic from each city in the tour
        for start_city in subset:
            temp_tour = [0]
            unvisited = list(subset)
            current_city = temp_tour[0]
            
            while unvisited:
                next_city = min(unvisited, key=lambda x: calculate_distance(cities[current_city], cities[x]))
                temp_tour.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city
            
            temp_tour.append(0)  # complete the tour by returning to the depot
            current_distance = tour_distance(temp_tour)
            
            # Check if we have found a new shorter tour
            if current_distance < minimum_distance:
                minimum_distance = current_distance
                best_tour = temp_tour
            
    return best_tour, minimum_time

# Run the function to find the shortest tour
calculated_tour, calculated_cost = find_shortest_tour()

# Display results
print("Tour:", calculated_tour)
print("Total travel cost:", calculated_cost)