import math

# Define all city coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), 
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), 
          (21, 21), (12, 39)]

# Group mapping, each group lists the cities included in that group
groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def select_nearest_from_group(depot, group):
    """Select the nearest city from a group to the depot."""
    nearest_city = min(group, key=lambda x: euclidean_distance(cities[depot], cities[x]))
    return nearest_city

def calculate_tour_length(tour):
    """Calculate the total length of the given tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Initialize tour starting with the depot
tour = [0]

# Select the nearest city from each group to the depot
for group in groups:
    nearest_city = select_nearest_from_group(0, group)
    tour.append(nearest_city)

# Closing the loop by returning to depot
tour.append(0)

# Calculate the total travel cost of the tour
total_cost = calculate_tour_length(tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")