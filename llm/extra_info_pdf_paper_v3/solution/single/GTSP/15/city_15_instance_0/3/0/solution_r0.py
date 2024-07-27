import itertools
import math

# Define the cities with their coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), 
          (60, 55), (4, 39)]

# Define the city groups
city_groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generate all possible tours that visit one city from each group and return to the depot
possible_tours = itertools.product(*city_groups)

minimum_cost = float('inf')
best_tour = []

# Checking every possible combination of cities to get the shortest possible route
for tour in possible_tours:
    # Include the depot as the start and end point
    complete_tour = [0] + list(tour) + [0]
    
    # Calculate the travel cost for the current tour
    travel_cost = sum(distance(complete_tour[i], complete_tour[i+1]) for i in range(len(complete_tour)-1))
    
    # Check if the found tour is shorter than the found so far
    if travel_cost < minimum_cost:
        minimum_cost = travel_cost
        best_tour = complete_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(minimum_cost, 2))