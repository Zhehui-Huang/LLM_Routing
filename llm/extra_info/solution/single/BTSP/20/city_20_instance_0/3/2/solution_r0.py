import math

# City coordinates
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
          (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
          (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
          (60, 63), (93, 15)]

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all pairwise distances
num_cities = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] 
             for i in range(num_cities)]

# Function to find tour minimizing the maximum edge length
def find_min_max_tour(start_city):
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(nextcity)
        current_city = next_city
    
    tour.append(start_city)  # Return to the start city
    return tour

# Calculate the tour from the depot (city 0)
tour = find_min_max_tour(0)

# Calculate the total travel cost and the maximum distance between consecutive cities
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")