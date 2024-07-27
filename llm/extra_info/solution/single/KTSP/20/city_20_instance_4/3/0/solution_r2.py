import itertools
import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Define city coordinates including the depot
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Precompute the distance between all pairs of cities
distances = [[calculate_distance(cities[i], cities[j]) for j in range(20)] for i in range(20)]

# Function to find a route using a greedy approach starting from the depot, visiting 15 additional unique cities
def greedy_route(city_selection):
    current_city = 0
    visited = [False] * 20
    visited[0] = True
    tour = [0]
    
    for _ in range(15):  # Only add 15 others, total 16 including depot
        next_city = None
        min_dist = float('inf')
        for city in city_selection:
            if not visited[city] and distances[current_city][city] < min_dist:
                min_dist = distances[current_city][city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_city
    tour.append(0)  # Return to depot
    return tour

# Find the minimum cost tour
min_cost = float('inf')
best_tour = None

# Evaluate only selections of 15 cities other than the depot
for selection in itertools.combinations(range(1, 20), 15):
    tour = greedy_route(selection)
    cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")