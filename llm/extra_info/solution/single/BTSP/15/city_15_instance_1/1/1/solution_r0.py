import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = eu.addObjective(distanceLock)

# Initial tour starts and ends at the depot city 0
tour = [0, 0]  # Start and end at the depot
max_distance_in_tour = 0

# Find the city that minimizes the maximum leg distance when inserted
def find_best_insertion(tour):
    best_city = None
    best_position = None
    best_max_leg = float('inf')
    best_total_cost = float('inf')
    
    remaining_cities = set(range(1, n)) - set(tour[:-1])
    
    for city in remaining_cities:
        for i in range(1, len(tour)):
            current_tour = tour[:i] + [city] + tour[i:]
            total_cost = sum([distances[current_tour[j]][current_tour[j + 1]] for j in range(len(current_tour) - 1)])
            max_leg = max([distances[current_tour[j]][current_tour[j + 1]] for j in range(len(current_tour) - 1)])
            if max_leg < best_max_leg or (max_leg == best_max_leg and total_cost < best_total_cost):
                best_city = city
                best_position = i
                best_max_leg = max_leg
                best_total_cost = total_cost
    
    return best_city, best_position, best_max_leg, best_total_pmtrices[(tour[u])cities[tour))

while len(set(tour) - set([0])) < n - 1:
    city, position, max_distance_in_tour, _ = find_best_insertion(tour)
    tour = tour[:position] + [city] + tour[position:]

# Calculate the final total travel cost
total_travel_cost = sum([distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_in_tour}")