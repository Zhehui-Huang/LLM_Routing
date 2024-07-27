import numpy as np

# Define the cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculating distances between all pairs of cities
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Helper function to calculate the tour cost
def tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Implementing a greedy approach to select 13 cities (including depot)
def find_minimal_tour():
    selected_cities = [0]  # Always start at the depot city
    visited = set(selected_cities)

    # Greedily add close cities until we have 13 cities
    while len(selected_cities) < 13:
        last_city = selected_cities[-1]
        next_city = min([(i, distances[last_city][i]) for i in range(n) if i not in visited],
                        key=lambda x: x[1])[0]
        selected_cities.append(next_city)
        visited.add(next_city)

    # End tour at the depot city
    selected_cities.append(0)

    return selected_cities

# Generate a tour
tour = find_minimal_tour()
total_cost = tour_cost(tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")