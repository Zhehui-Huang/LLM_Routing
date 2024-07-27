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

# Function for Nearest Neighbor Algorithm to choose k cities including the depot
def generate_tour_with_nearest_neighbor(depot, selected_cities):
    # Start from the depot
    tour = [depot]
    unvisited = set(selected_cities) - set(tour)
    
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)

    # Return to depot to complete the tour
    tour.append(depot)
    return tour

# Determine the selection of cities including the depot city
selected_cities = [0]  # start with the depot city

# Accumulate distances to all other cities from the depot
near_cities = sorted([(distance(0, i), i) for i in range(1, 20)])
selected_cities.extend([x[1] for x in near_cities[:15]])  # pick 15 nearest cities next to the depot

# Generate the tour using nearest neighbor algorithm
tour = generate_tour_with_nearest_neighbor(0, selected_cities)

# Total travel cost calculation
total_travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)