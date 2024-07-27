import math

# Define coordinates of the cities
city_coords = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Stores the distance from each city to every other city (memoization)
distances = {}
for i in range(len(city_coords)):
    distances[i] = {}
    for j in range(len(city_coords)):
        distances[i][j] = euclidean_distance(city_coords[i], city_coords[j])

# Nearest Neighbor algorithm
def nearest_neighbor(start_city):
    unvisited = set(range(1, len(city_coords)))  # Exclude depot initially
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_kcity

    # Returning to the start city (depot)
    tour.append(start_city)
    return tour

# Calculate the tour starting from depot city 0
tour = nearest_neighbor(0)

# Calculate the total travel cost of the tour
total_travel_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")