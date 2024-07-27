import math
from itertools import combinations

# Define the cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Function for Nearest Neighbor Algorithm
def nearest_neighbor(k, start_city):
    visited = [start_city]
    unvisited = set(range(k)) - set(visited)
    
    while unconnected:
        last_city = visited[-1]
        next_city = min(unconnected, key=lambda x: distance(last_city, x))
        visited.append(next_city)
        unconnected.remove(next_city)
    
    return visited

# Select 15 closest other cities from the depot
k = 16
city_distances = [(distance(0, i), i) for i in range(1, 20)]
city_distances.sort()  # Sort cities based on distance from depot
selected_cities = [city[1] for city in city_distance[:k-1]]  # Select 15 closest cities
selected_cities.insert(0, 0)  # Include the depot as the start and end point

tour = nearest_neighbor(selected_cities)

# Complete tour by returning to the start city
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)